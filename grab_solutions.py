#!/usr/bin/env python3
import requests, re
from getpass import getpass

def main():
    # login
    login_url = 'https://leetcode.com/accounts/login/'
    print('Login to leetcode...')
    username = input('username: ')
    password = getpass('password: ')

    session = requests.Session()

    response = session.request('GET', login_url)
    if response.status_code != 200 or not session.cookies['csrftoken']:
        print('Error in get login page')
        print(response.status_code)
        print(response.text)
        return

    login_data = {
            'csrfmiddlewaretoken': session.cookies['csrftoken'],
            'login': username,
            'password': password
            }
    headers = {
            'Referer': login_url,
            'x-requested-with': 'XMLHttpRequest',
            }
    response = session.request('POST', login_url, headers = headers, data = login_data)

    if response.status_code == 200 and 'Successfully signed in' in response.headers['Set-Cookie']:
        print('Logged in')
    else:
        print('Error in log in')
        print(response.status_code)
        print(response.text)
        return

    # get problem list
    query = {
            "operationName": "allQuestions",
            "variables": {},
            "query": "query allQuestions {\n  allQuestions {\n    ...questionSummaryFields\n    __typename\n  }\n}\n\nfragment questionSummaryFields on QuestionNode {\n  title\n  titleSlug\n  translatedTitle\n  questionId\n  questionFrontendId\n  status\n  difficulty\n  isPaidOnly\n  __typename\n}\n"
            }
    response = session.request('POST', 'https://leetcode.com/graphql', headers = headers, json = query)
    if response.status_code == 200:
        print('Got problem list')
    else:
        print('Error get problem list')
        print(response.status_code)
        print(response.text)
        return
    problems = response.json()['data']['allQuestions']

    # input problem ids to grab
    s = input('Input problem ids to download(0 means all): ')
    if s == '0':
        ids = [n + 1 for n in range(len(problems)) if problems[n]['status'] == 'ac']
    else:
        ids = [int(n) for n in s.split()]

    for id in ids:
        problem = problems[id - 1]
        print('Download #%d %s' % (id, problem['title']))

        # get submission list
        query = {
                "operationName": "Submissions",
                "variables": {
                    "offset": 0,
                    "limit": 20,
                    "lastKey": None,
                    "questionSlug": problem['titleSlug']
                    },
                "query": "query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      statusDisplay\n      lang\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      __typename\n    }\n    __typename\n  }\n}\n"
                }
        response = session.request('POST', 'https://leetcode.com/graphql', headers = headers, json = query)
        if response.status_code == 200:
            print('Got submission list')
        else:
            print('Error get submission list')
            print(response.status_code)
            print(response.text)
            continue
        submissions = response.json()['data']['submissionList']['submissions']

        latest_accepted = {}
        extension = {
                'python3': 'py',
                'cpp': 'cpp',
                'javascript': 'js'
                # Add other lang
                }
        for s in submissions:
            if s['statusDisplay'] == 'Accepted' and s['lang'] not in latest_accepted:
                latest_accepted[s['lang']] = s

        # get ac code
        for submission in latest_accepted.values():
            url = 'https://leetcode.com' + submission['url']
            filename = str(id) + '.' + problem['titleSlug'] + '.' + extension[submission['lang']]
            response = session.request('GET', url, headers = headers)
            if response.status_code != 200:
                print('Error get code')
                print(response.status_code)
                print(response.text)
                continue
            match = re.search('submissionCode: \'(.*)\',', response.text)
            if not match[1]:
                print('Error get code')
                print(response.text)
                continue

            print('Got %s submission' % (submission['lang']))
            code = bytes(match[1], 'ascii').decode('unicode-escape')

            # write to file
            with open(filename, 'w') as fp:
                fp.write(code)
            print('Wrote to ' + filename)
    print('Finish')

if __name__ == '__main__':
    main()

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            if s == "0":
                return True
            if s[0] == '0':
                return False
            return int(s) < 256
        ans = []
        n = len(s)
        r = [1, 2, 3]
        for a in r:
            for b in r:
                for c in r:
                    for d in r:
                        if a + b + c + d == n:
                            s1 = s[:a]
                            s2 = s[a:a + b]
                            s3 = s[a + b:a + b + c]
                            s4 = s[a + b + c:]
                            if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
                                ans.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
        return ans;
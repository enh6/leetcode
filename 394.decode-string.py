class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = []
        i = 0
        while i < len(s):
            if s[i].isalpha():
                result.append(s[i])
            elif s[i] == ']':
                (n, prev) = stack.pop()
                result = prev + result * n
            else:
                n = 0
                while s[i] != '[':
                    n = n * 10 + int(s[i])
                    i = i + 1
                stack.append((n, result))
                result = []
            i = i + 1
        return ''.join(result)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        result = [0] * len(s)
        i = -1
        while i < len(s):
            if i < 0 or result[i] == 1:
                for j in range(1, 20):
                    if i+1+j <= len(s) and s[i+1:i+1+j] in wordDict:
                        result[i+j] = 1
            i += 1
        if result[-1] == 1:
            return True
        else:
            return False

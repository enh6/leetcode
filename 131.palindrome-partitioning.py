class Solution:
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        result = []
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                lists = self.partition(s[i+1:])
                for l in lists:
                    result.append([s[:i+1]] + l)
        return result
        

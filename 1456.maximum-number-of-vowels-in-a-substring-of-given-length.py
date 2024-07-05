class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = 0
        for i in range(k):
            if s[i] in vowels:
                n = n + 1
        m = n
        for i in range(k, len(s)):
            if s[i] in vowels:
                n = n + 1
            if s[i-k] in vowels:
                n = n - 1
            if n > m:
                m = n
        return m

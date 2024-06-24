class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        from collections import Counter
        l = len(p)
        p = Counter(p)
        c = Counter(s[:l])
        i = 0
        if p == c:
            result.append(i)
        while i < len(s) - l:
            c[s[i]] = c[s[i]] - 1
            c[s[i+l]] = c[s[i+l]] + 1
            i = i + 1
            if p == c:
                result.append(i)
        return result

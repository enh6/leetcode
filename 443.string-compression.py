class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        prev = chars[0]
        count = 1
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == prev:
                count = count + 1
            else:
                chars[idx] = prev
                idx = idx + 1
                if count > 1:
                    for char in str(count):
                        chars[idx] = char
                        idx = idx + 1
                if i < len(chars):
                    prev = chars[i]
                    count = 1
        return idx

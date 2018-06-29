class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(words):
            width = len(words[i])
            line = words[i]
            j = i + 1
            while j < len(words) and width + len(words[j]) + 1 <= maxWidth:
                width = width + len(words[j]) + 1
                j += 1
            if j == i + 1 or j == len(words):
                for k in range(i + 1, j):
                    line = line + " " + words[k]
                line = line.ljust(maxWidth)
            else:
                mod = (maxWidth - width) % (j - 1 - i)
                space_count = (maxWidth - width) // (j - 1 - i) + 1
                for k in range(i + 1, i + 1 + mod):
                    line = line + " " * (space_count + 1) + words[k]
                for k in range(i + 1 + mod, j):
                    line = line + " " * (space_count) + words[k]
            ans.append(line)
            i = j;
        return ans;
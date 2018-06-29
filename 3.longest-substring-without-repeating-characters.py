class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        begin = -1
        char_dict = {}
        for i, c in enumerate(s):
            if c in char_dict and char_dict[c] > begin:
                begin = char_dict[c]
            char_dict[c] = i
            max_length = max(max_length, i - begin)
        return max_length
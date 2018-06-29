class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = [0] * 128
        for c in t:
            map[ord(c)] += 1
        begin, end, count = 0, 0, 0
        win_head, win_len = 0, len(s) + 1
        while end < len(s):
            map[ord(s[end])] -= 1
            if map[ord(s[end])] >= 0:
                count += 1
            if count == len(t):
                while map[ord(s[begin])] < 0:
                    map[ord(s[begin])] += 1
                    begin += 1
                if end - begin + 1 < win_len:
                    win_len = end - begin + 1
                    win_head = begin
                map[ord(s[begin])] += 1
                begin += 1
                count -= 1
            end += 1
        return s[win_head : win_head + win_len] if win_len <= len(s) else ""
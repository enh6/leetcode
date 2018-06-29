class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret = []
        wl = len(words[0])
        wc = len(words)
        if len(s) < wl * wc:
            return ret
        occurs = {}
        for w in words:
            if w in occurs:
                occurs[w] += 1
            else:
                occurs[w] = 1
        for i in range(len(s) - wl * wc + 1):
            occ = {}
            cnt = 0
            for j in range(wc):
                w = s[i + j * wl:i + j * wl + wl]
                if not w in occurs:
                    break
                else:
                    if w in occ:
                        occ[w] += 1
                    else:
                        occ[w] = 1
                    if occ[w] == occurs[w]:
                        cnt += 1
                    elif occ[w] > occurs[w]:
                        break
            if cnt == len(occurs):
                ret.append(i)
        return ret
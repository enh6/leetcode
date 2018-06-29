class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {};
        for str in strs:
            key = "".join(sorted(str))
            if key in groups:
                groups[key].append(str)
            else:
                groups[key] = [str]
        return [groups[key] for key in groups]
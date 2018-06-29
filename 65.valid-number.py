class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # \s* space
        # \d+(\.\d*)?|\.\d+ float
        # [+-]?\\d+ integer
        return re.match(r"^\s*[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?\s*$", s) != None
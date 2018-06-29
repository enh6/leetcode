class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strs = []
        if not digits:
            return strs
        init_str = ""
        lut = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        for c in digits:
            init_str +=  lut[c][0]
        strs.append(init_str)
        for i in range(len(digits)):
            for str in strs[:len(strs)]:
                replace = lut[digits[i]]
                for c in replace[1:]:
                    strs.append(str[:i] + c + str[i + 1:])
        return strs
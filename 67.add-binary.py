class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            return self.addBinary(b, a)
        c = 0
        sum = ""
        j = len(b) - 1
        for i in range(len(a) - 1, -1, -1):
            if a[i] == '1':
                c += 1
            if j >= 0 and b[j] == '1':
                c += 1
            if c % 2 == 1:
                sum = '1' + sum
            else:
                sum = '0' + sum
            c = c // 2
            j -= 1
        if c:
            return "1" + sum
        else:
            return sum;
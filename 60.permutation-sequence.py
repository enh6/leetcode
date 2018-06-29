class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        nums = []
        ans = ""
        total = 1
        for i in range(1, n + 1):
            total = total * i
            nums.append(i)
        for i in range(n, 0, -1):
            total = total // i
            j = k // total
            k = k % total
            ans += str(nums[j])
            del nums[j]
        return ans
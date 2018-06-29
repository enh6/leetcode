class Solution:
    def combination(self, candidates, target, pos, current, ans):
        if target == 0:
            ans.append(current[:])
            return
        if target < 0:
            return
        for i in range(pos, len(candidates)):
            current.append(candidates[i])
            self.combination(candidates, target - candidates[i], i, current, ans)
            current.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        current = []
        self.combination(candidates, target, 0, current, ans)
        return ans
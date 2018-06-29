class Solution:
    def combination(self, candidates, target, pos, current, ans):
        if target == 0:
            ans.append(current[:])
            return
        if target < 0:
            return
        for i in range(pos, len(candidates)):
            if i > pos and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            self.combination(candidates, target - candidates[i], i + 1, current, ans)
            current.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.combination(candidates, target, 0, [], ans)
        return ans
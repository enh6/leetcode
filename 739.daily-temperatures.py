class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result = [0] * l
        idx = l - 1

        stack = []
        while idx >= 0:
            t = temperatures[idx]
            while stack and stack[-1][0] <= t:
                stack.pop()
            if not stack:
                result[idx] = 0
            else:
                result[idx] = stack[-1][1] - idx
            stack.append((t, idx))
            idx = idx - 1
        return result

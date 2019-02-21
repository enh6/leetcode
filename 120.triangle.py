class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        sums = triangle[0];
        for i in range(1, len(triangle)):
            row = triangle[i]
            new_sums = [0] * len(row)
            new_sums[0] = sums[0] + row[0]
            for j in range(1, len(row) - 1):
                new_sums[j] = min(sums[j - 1], sums[j]) + row[j]
            new_sums[-1] = sums[-1] + row[-1]
            sums = new_sums
        return min(sums)

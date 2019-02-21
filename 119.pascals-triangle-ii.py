class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        row = []
        for i in range(rowIndex + 1):
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j - 1] + row[j]
        return row

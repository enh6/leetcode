class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            pos_list = []
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    if c in pos_list:
                        return False
                    else:
                        pos_list.append(c)
        for i in range(9):
            pos_list = []
            for j in range(9):
                c = board[j][i]
                if c != '.':
                    if c in pos_list:
                        return False
                    else:
                        pos_list.append(c)
        for i in range(9):
            pos_list = []
            for j in range(9):
                c = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if c != '.':
                    if c in pos_list:
                        return False
                    else:
                        pos_list.append(c)
        return True
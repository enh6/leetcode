class Solution:
    def solve(self, board, state, i_begin, j_begin):
        for i in range(i_begin, 9):
            for j in range(i_begin, 9):
                if board[i][j] == '.':
                    pos = j // 3 * 3 + i // 3
                    for n in range(9):
                        if state[0][i][n] == False and state[1][j][n] == False and state[2][pos][n] == False:
                            board[i][j] = str(1 + n)
                            state[0][i][n] = True
                            state[1][j][n] = True
                            state[2][pos][n] = True
                            if self.solve(board, state, i_begin, j_begin):
                                return True
                            state[0][i][n] = False
                            state[1][j][n] = False
                            state[2][pos][n] = False
                    board[i][j] = '.'
                    return False
        return True;

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        state = [[[False for _ in range(9)] for _ in range(9)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    pos = ord(board[i][j]) - ord('1')
                    state[0][i][pos] = True
                    state[1][j][pos] = True
                    state[2][j // 3 * 3 + i // 3][pos] = True
        self.solve(board, state, 0, 0)
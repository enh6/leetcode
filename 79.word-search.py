class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def exist_helper(x, y, i):
            if i == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            if board[x][y] != word[i]:
                return False
            c = board[x][y]
            board[x][y] = 0
            exists =  exist_helper(x + 1, y, i + 1) \
                      or exist_helper(x, y + 1, i + 1) \
                      or exist_helper(x - 1, y, i + 1) \
                      or exist_helper(x, y - 1, i + 1)
            board[x][y] = c
            return exists
        for x in range(len(board)):
            for y in range(len(board[0])):
                if exist_helper(x, y, 0):
                    return True
        return False
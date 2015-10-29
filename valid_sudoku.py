
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            horiz, vert = dict(), dict()
            for j in xrange(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in horiz:
                    return False
                elif board[j][i] in vert:
                    return False
                else:
                    horiz[board[i][j]] = True
                if board[j][i] == '.':
                    False
                elif board[j][i] in vert:
                    return False
                else:
                    vert[board[j][i]] = True
        # Check sub-boxes
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                d = {}
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        if board[i][j] == '.':
                            pass
                        elif board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        return True
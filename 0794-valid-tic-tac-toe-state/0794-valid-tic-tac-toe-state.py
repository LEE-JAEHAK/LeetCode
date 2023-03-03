class Solution(object):
    def finishX(self, board):
        if   board[0][0] == board[0][1] == board[0][2] and board[0][0] == 'X':
            return True
        elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == 'X':
            return True
        elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == 'X':
            return True
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'X':
            return True
        elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == 'X':
            return True
        elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == 'X':
            return True
        elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == 'X':
            return True
        elif board[2][0] == board[1][1] == board[0][2] and board[2][0] == 'X':
            return True
        return False
    
    def finishO(self, board):
        if   board[0][0] == board[0][1] == board[0][2] and board[0][0] == 'O':
            return True
        elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == 'O':
            return True
        elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == 'O':
            return True
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'O':
            return True
        elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == 'O':
            return True
        elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == 'O':
            return True
        elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == 'O':
            return True
        elif board[2][0] == board[1][1] == board[0][2] and board[2][0] == 'O':
            return True
        return False

    def counts(self, board):
        a,b = 0,0
        for i in board:
            for j in range(3):
                if i[j] == 'X':
                    a += 1
                elif i[j] == 'O':
                    b += 1
        return a,b
     
    def validTicTacToe(self, board):
        x,y = self.counts(board)
        print(x,y)
        if (x == y or x == y+1):
            pass
        else:
            return False

        ans = self.finishX(board)
        if ans and x != y+1:
            return False
        
        elif self.finishO(board) and x != y:
            return False

        return True
        """
        :type board: List[str]
        :rtype: bool
        """
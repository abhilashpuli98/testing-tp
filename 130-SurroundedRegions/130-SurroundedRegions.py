# Last Updated: 2/5/2026, 9:25:00 AM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        letter='O'
        new_letter='A'
        def capture(i,j):
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!='O':
                return
            board[i][j]='A'
            capture(i,j+1)
            capture(i,j-1)
            capture(i+1,j)
            capture(i-1,j)
        for r in range(m):
            if board[r][0]=='O':
                capture(r,0)
            if board[r][n-1]=='O':
                capture(r,n-1)
        for c in range(n):
            if board[0][c]=='O':
                capture(0,c)
            if board[m-1][c]=='O':
                capture(m-1,c)
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='A':
                    board[r][c]='O'
        return board
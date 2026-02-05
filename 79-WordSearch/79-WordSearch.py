# Last Updated: 2/5/2026, 9:25:26 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def backtrack(curr_row,curr_col,let_indx):
            if let_indx==len(word):
                return True
            if curr_row>=rows or curr_row<0 or curr_col<0 or curr_col>=cols or word[let_indx]!=board[curr_row][curr_col]:
                return False
            temp=board[curr_row][curr_col]
            board[curr_row][curr_col]=None
            if backtrack(curr_row+1,curr_col,let_indx+1) or backtrack(curr_row-1,curr_col,let_indx+1) or backtrack(curr_row,curr_col+1,let_indx+1) or backtrack(curr_row,curr_col-1,let_indx+1):
                return True
            board[curr_row][curr_col]=temp
            return False
        def find_word():
            for i in range(rows):
                for j in range(cols):
                    if backtrack(i,j,0):
                        return True
            return False
        return find_word()
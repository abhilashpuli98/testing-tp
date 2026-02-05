# Last Updated: 2/5/2026, 9:22:25 AM
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows=[0]*3
        cols=[0]*3
        diag=0
        adiag=0
        for i,(r,c) in enumerate(moves):
            player=-1 if i%2==0 else 1

            rows[r]+=player
            cols[c]+=player
            if r==c:
                diag+=player
            if r+c==2:
                adiag+=player
            if abs(diag)==3 or abs(adiag)==3 or abs(rows[r])==3 or abs(cols[c])==3:
                return 'A' if player == -1 else 'B'
        return 'Draw' if len(moves)==9 else 'Pending'
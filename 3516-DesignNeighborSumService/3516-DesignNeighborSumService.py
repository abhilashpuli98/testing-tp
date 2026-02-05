# Last Updated: 2/5/2026, 9:21:15 AM
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.length = len(grid)
        self.positions = {grid[i][j] :(i,j) for i in range(self.length) for j in range(self.length) }

    def adjacentSum(self, value: int) -> int:
        result = 0
        i,j = self.positions[value]
        track = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
        for x,y in track:
            if 0<=x<self.length and 0<=y<self.length:
                result+=self.grid[x][y]
        return result

    def diagonalSum(self, value: int) -> int:
        i,j = self.positions[value]
        track = [[i-1,j-1],[i+1,j+1],[i-1,j+1],[i+1,j-1]]
        result = 0
        for x,y in track:
            if 0<=x<self.length and 0<=y<self.length:
                result+=self.grid[x][y]
        return result


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
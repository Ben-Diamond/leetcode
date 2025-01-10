class Solution:
    def numMagicSquaresInside(self, grid):
        width = len(grid[0])
        height = len(grid)
        
        # if width < 3 or height < 3:
        #     return 0
        digits = set([1,2,3,4,5,6,7,8,9])
        total = 0
        for y in range(0,height - 2):
            for x in range(0,width-2):

                numbers = set(grid[y][x:x+3] + grid[y+1][x:x+3] + grid[y+2][x:x+3])
                if numbers != digits:
                    continue
                #row, column, both diagonals must share a sum
                squareSum = grid[y][x] + grid[y][x+1] + grid[y][x+2]# top 
                if (squareSum == grid[y][x] + grid[y+1][x] + grid[y+2][x] and #left
                squareSum == grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2] and #diagonal
                squareSum == grid[y][x+1] + grid[y+1][x+1] + grid[y+2][x+1] and #middle row
                squareSum == grid[y][x+2] + grid[y+1][x+2] + grid[y+2][x+2] and #right
                squareSum == grid[y+2][x] + grid[y+2][x+1] + grid[y+2][x+2] and #bottom
                squareSum == grid[y][x+1] + grid[y+1][x+1] + grid[y+2][x+1] and #middle column
                squareSum == grid[y+2][x] + grid[y+1][x+1] + grid[y][x+2]): #other diagonal
                    total += 1
                
        return total


solver = Solution.__new__

grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]

grid = [[5,5,5],[5,5,5],[5,5,5]]
print(Solution.numMagicSquaresInside(solver,grid))

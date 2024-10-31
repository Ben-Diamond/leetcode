class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        x,y = cStart,rStart
       
        distance = 1
        direction = 0
        moves = [
            lambda x,y: (x+1,y) ,
            lambda x,y: (x,y+1) ,
            lambda x,y: (x-1,y) ,
            lambda x,y: (x,y-1)
        ]

        visitedInGrid = []
        while len(visitedInGrid) < rows*cols:
             # move, turn, move, turn, increment distance
            for b in range(2):
                for c in range(distance):
                    if x >=0 and x < cols and y>=0 and y < rows:
                        visitedInGrid.append([y,x])
                    x,y = moves[direction](x,y)

                direction = (direction + 1)%4
            distance += 1
        return visitedInGrid
    
solver = Solution.__new__

rows,cols,rStart,cStart = 5,6,1,4
print(Solution.spiralMatrixIII(solver,rows,cols,rStart,cStart))
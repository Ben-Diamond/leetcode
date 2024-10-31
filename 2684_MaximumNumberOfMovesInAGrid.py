class Solution:
    def maxMoves(self, grid) -> int:
        
        """
        (y,x) -> (y+-1, x+1)
        but must be bigger
        only current location matters
        progress all by t
        """
        m,n = len(grid),len(grid[0])
        paths = set()
        for x in range(m):
            paths.add(x)

        for t in range(n-1):
            newpaths = set()


            for p in paths:
                current = grid[p][t]
                if grid[p][t+1] > current:
                    newpaths.add(p)
                if p>0 and grid[p-1][t+1] > current:
                    newpaths.add(p-1)
                if p<m-1 and grid[p+1][t+1] > current:
                    newpaths.add(p+1)

            if len(newpaths) == 0:
                return t
            

            paths = newpaths.copy()
        return t + 1

grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid = [[3,2,4],[2,1,9],[1,1,7]]
solver = Solution.__new__
print(Solution.maxMoves(solver,grid))


#beat 100% / 98%
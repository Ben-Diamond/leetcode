class Solution:
    def minDays(self, grid) -> int:
        #check if it is already split
        #if not, remove a sand and check if it is split
        #the answer is never more than two so no need for further checks

        sands = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    sands.add((x,y))
        #breadth first is the easiest way to check if it is already split

        def checkAttached(sands,ignore):
            start = ignore
            while start == ignore:
                start = sands.pop()
                sands.add(start) #get something

            new = [start]
            visited = set()


            visited.add(start)
            while new != []:
                q = new.copy()
                new = []
                for sand in q:
                    x,y = sand
                    for nextSand in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
                        if nextSand in sands and nextSand not in visited:
                            visited.add(nextSand)
                            if nextSand != ignore:
                                new.append(nextSand)
            print(visited)
            return len(visited) == len(sands)
        
        if len(sands) <= 2:
            return len(sands)
        
        if not checkAttached(sands,(-1,-1)):
            return 0
        


        for sand in sands:
            x,y = sand
            if not checkAttached(sands,sand):
                return 1
            
        return 2

solver = Solution.__new__


grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
grid = [[0,1,0,1]]

print(Solution.minDays(solver,grid))
"""
...##.
...##.
..##..
..##..

"""
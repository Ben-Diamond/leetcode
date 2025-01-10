
"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '.
 These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
"""
"""
/\
\/
becomes
o--o
-oo-
-oo-
o--o

oo-
o-o
-oo

-oo
o-o
oo-

and pathfind out
"""
#//
#/ 
class Solution:
    def regionsBySlashes(self, grid):
        #get -o form
        openSpaces = set()
        for y in range(len(grid)):
            for x in range(len(grid)): #lol its the same
                if grid[y][x] == "/":
                    openSpaces.update([
                        (3*x,3*y,),
                        (3*x+1,3*y,),
                        (3*x,3*y+1,),
                        (3*x+1,3*y+2,),
                        (3*x+2,3*y+1,),
                        (3*x+2,3*y+2,),       
                                       ])
                    # openSpaces.add((2*x + 1,2*y + 1))
                elif grid[y][x] == " ":
                    openSpaces.update([
                        (3*x,3*y,),
                        (3*x+1,3*y,),
                        (3*x,3*y+1,),
                        (3*x+1,3*y+2,),
                        (3*x+2,3*y+1,),
                        (3*x+2,3*y+2,),
                        (3*x+1,3*y+1,), 
                        (3*x,3*y+2,), 
                        (3*x+2,3*y),   
                                       ])
                else:
                    #the \
                    openSpaces.update([
                        (3*x+1,3*y,),
                        (3*x,3*y+1,),
                        (3*x+1,3*y+2,),
                        (3*x+2,3*y+1,),
                        (3*x,3*y+2,), 
                        (3*x+2,3*y),       
                                       ])
        
        usedInPath = set()
        total = 0
        print(openSpaces)

        out = ""
        for y in range(len(grid)*3):
            for x in range(len(grid)*3):
                if (x,y) in openSpaces:
                    out += "o"
                else:
                    out += "-"
            out += "\n"
        print(out)

        for startPoint in openSpaces:
            if startPoint in usedInPath: 
                continue
            total += 1

            next = [startPoint]

            while next != []:
                current = next.copy()
                next = []
                for point in current:
                    x,y = point
                    for newPoint in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                            
                        if newPoint in openSpaces and newPoint not in usedInPath:
                            next.append(newPoint)
                            usedInPath.add(newPoint)

            #now pathfind our way to everything
        print(total)
        print(usedInPath)

        return total

solver = Solution.__new__


grid = ["//","/ "]
"""
o-o-
-o-o
o-oo
-ooo

"""
print(Solution.regionsBySlashes(solver,grid))

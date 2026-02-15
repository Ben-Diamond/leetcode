class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # glasses[i][j] contains row i, glass j
        # because it is left-based, each glass pours below and to its right
        # sincen not time dependent, go row by row and add in liquid
        glasses = [[0. for j in range(i+1)] for i in range(query_row + 1)] #don't need to go past query_row
        glasses[0][0] = float(poured)
        
        for i in range(query_row):
            #emptying row i; do not need to go further
            for j in range(i + 1):
                liquid = glasses[i][j]
                if liquid > 1:
                    glasses[i+1][j] += (liquid-1)/2
                    glasses[i+1][j+1] += (liquid-1)/2
        return min(1., glasses[query_row][query_glass])
    


solver = Solution()
poured = 100000009
query_row = 33
query_glass = 17

print(solver.champagneTower(poured, query_row, query_glass))
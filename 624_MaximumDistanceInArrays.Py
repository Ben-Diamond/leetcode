"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

MINE IS AN O(N) SOLUTION; PLACED ABOVE 95-100% BECAUSE THEY DO WORSE
"""

class Solution:
    def maxDistance(self, arrays) -> int:
            
        

        def getExtremes(lowIgnore,highIgnore):
            lowest, highest,lowIndex,highIndex = +10e5, -10e5,-1,-1
            for a,arr in enumerate(arrays):
                if arr[0] < lowest and a != lowIgnore:
                    lowest = arr[0]
                    lowIndex = a
                if arr[-1] > highest and a != highIgnore:
                    highest = arr[-1]
                    highIndex = a
            return lowest, highest,lowIndex,highIndex
        
        lowest, highest,lowIndex,highIndex = getExtremes(-1,-1)

        if lowIndex != highIndex:
            return highest - lowest
        #the answer will always involve either the lowest or highest number
        #so try using either from the contested array

        lowest, highest,lowIndex,highIndex = getExtremes(-1,highIndex)
        #use the lower number
        result1 = highest - lowest
        lowest, highest,lowIndex,highIndex = getExtremes(lowIndex,-1)
        #use the higher number (the lowIndex will be the same)
        result2 = highest - lowest
        if result1 > result2:
            return result1
        return result2
        # return lowest,highest,lowIndex,highIndex

solver = Solution.__new__
arrays = [[1,2,3],[4,5],[1,2,3]]*3333333


print(Solution.maxDistance(solver,arrays))
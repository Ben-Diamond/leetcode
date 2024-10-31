"""
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. 
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""


class Solution:
    def canBeEqual(self, target, arr) -> bool:
        #return all([target.count(x) == arr.count(x) for x in target])
        #above is a one liner
        targetAmounts = {}
        arrAmounts = {}
        for num in target:
            if num not in targetAmounts:
                targetAmounts[num] = 0

            targetAmounts[num] += 1
        for num in arr:
            if num not in targetAmounts: 
                return False
            if num not in arrAmounts:
                arrAmounts[num] = 0
            arrAmounts[num] += 1
            if arrAmounts[num] > targetAmounts[num]: 
                return False
            #this works because if they are different, there must be more of something in arr than target
            #as their lengths are the same
        return True



solver = Solution.__new__

target= [1,2,3,4]
arr = [2,4,1,3]


print(Solution.canBeEqual(solver,target,arr))

target= [7]
arr = [7]
print(Solution.canBeEqual(solver,target,arr))

target= [3,7,9]
arr = [3,7,11]


print(Solution.canBeEqual(solver,target,arr))
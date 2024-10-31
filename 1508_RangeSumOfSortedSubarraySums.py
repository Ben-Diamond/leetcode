
"""
You are given the array nums consisting of n positive integers. 
You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, 
creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array.
Since the answer can be a huge number return it modulo 109 + 7.
"""

class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        #sliding window sum that reverses directions so its o(n^2)
        sums = []
        width = 1
        direction = 1
        currentSum = 0
        subStart = 0
        while width <= n:
            
            if subStart + direction * (width-1) == n or subStart + direction * (width-1) == -1:
                width += 1
                direction,subStart = [(),(-1,n-1),(1,0)][direction]
                continue
            currentSum += nums[subStart + direction * (width - 1)]
            if not((width < n and subStart == 0) or (width>1 and subStart == n-1)):
            
                currentSum -= nums[subStart - direction]
            sums.append(currentSum)
            subStart += direction
        sums = sorted(sums)
        return(sum(sums[left-1:right])% (10**9 + 7))

nums,n,left,right = [100]*1000,1000,1,500500

solver = Solution.__new__
print(Solution.rangeSum(solver,nums,n,left,right))
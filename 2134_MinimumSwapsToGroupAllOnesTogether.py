"""A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location."""


class Solution:
    def minSwaps(self, nums) -> int:

        length = len(nums)
        windowSize = nums.count(1)
        lowest = 10e5
        
        # windows = {}
        currentCount = 0 #number of ZEROS
        for n in range(length):
            if n == 0:
                currentCount = nums[0:windowSize].count(0)
            elif nums[n-1] == 1 and nums[(n + windowSize - 1)%length] == 0:
                currentCount += 1
            elif nums[n-1] == 0 and nums[(n + windowSize - 1)%length] == 1:
                currentCount -= 1
            if currentCount < lowest:
                lowest = currentCount
            # windows[n] = currentCount
        # print(windows)
        return lowest

solver = Solution.__new__



nums = [0,1,0,1,1,0,0]
print(Solution.minSwaps(solver,nums))

nums = [0,1,1,1,0,0,1,1,0]
print(Solution.minSwaps(solver,nums))

nums = [1,1,0,0,1]
print(Solution.minSwaps(solver,nums))

class Solution:
    def waysToSplitArray(self, nums) -> int:
        forwardSum = 0
        backwardSum = sum(nums)
        total = 0
        for i in range(len(nums) - 1):
            forwardSum += nums[i]
            backwardSum -= nums[i]
            if forwardSum >= backwardSum:         
                total += 1
        return total

solver = Solution.__new__
nums = [2,3,1,0]
print(Solution.waysToSplitArray(solver,nums))
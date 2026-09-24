class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            num:int = nums[i]
            val:int = 0

            while num > 0:
                val += num % 10
                num = num // 10

            if val == i:
                return i
            

        return -1

solver= Solution()

nums:list[int] = [1, 3, 2]
print(solver.smallestIndex(nums))


nums:list[int] = [1, 2, 3]
print(solver.smallestIndex(nums))


nums:list[int] = [1, 3, 2, 12]
print(solver.smallestIndex(nums))

nums:list[int] = [1, 10, 11]
print(solver.smallestIndex(nums))

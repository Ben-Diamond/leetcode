class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        total = 0
        prod = 1
        j = -1

        #at the end of each loop, j represents the end of the valid product from i
        #and prod is the last valid product
        #j increases so prod should be 1 and j can be i-1 (if invalid)

        for i in range(len(nums)):
            
            if j < i: #j could be i-2
                prod = 1
                j = i-1
            print(f"starting: {i} {j} prod {prod}")

            while True:
                if j+1 == len(nums) or prod*nums[j+1] >= k: #stop before incrementing j
                    prod = int(prod/nums[i])
                    break
                else:
                    j += 1
                    prod *= nums[j]

            
            total += max(j - i + 1,0)
        
        return total
    

# class Solution:
#     def numSubarrayProductLessThanK(self, nums, k: int) -> int:
#         # o(n^2)
#         # checking [i,j] with j on the inner loop going backwards
#         # nums[i] >= 1 so if [i,j] invalid then [i,l] invalid for all l>j
#         # also, if [i,j] valid then [i,l] valid for all i<=l<j
#         total = 0
#         for i in range(len(nums)):
#             prod = 1
#             for j in range(i,len(nums)):
#                 prod *= nums[j]
#                 if prod >= k:
#                     break
#                 total += 1
        
#         return total

    

solver = Solution()
nums = [10,5,2,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# nums = [2,100,3,4,6,100]
k = 100
print(solver.numSubarrayProductLessThanK(nums, k))
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # without binary conversion
        # subtract 2^0 and 2^2 and ... and 2^2k until it is 0
        # if it equals 0, is of the form 10101
        # same for 2^1 and 2^3 and ...
        # if it equals 0, it is of the form 1010

        k = n
        i = 0
        while k > 0:
            k -= 2**i
            i += 2
        if k == 0:
            return True
        
        k = n
        i = 1
        while k > 0:
            k -= 2**i
            i += 2
        if k == 0:
            return True
        return False

    

solver = Solution()
n = int("1010111",2)
print(n)
print(solver.hasAlternatingBits(n))
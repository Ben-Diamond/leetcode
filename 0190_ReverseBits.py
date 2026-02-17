class Solution:
    def reverseBits(self, n: int) -> int:

        return int(((bin(n).zfill(32)).replace("b", "0" if len(bin(n)) <= 32 else "")[::-1]),2)
        
    

solver=Solution()
n=43261596
print(solver.reverseBits(n))
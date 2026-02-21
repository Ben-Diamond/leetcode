class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        import numpy as np
        # get primes up to log2(right) since that's the number of digits
        primes = set()
        for x in range(2,int(np.floor(np.log2(right)))+1):
            prime = True
            for factor in range(2,int(np.floor(np.sqrt(x)))+1):
                if x % factor == 0:
                    prime = False
            if prime:
                primes.add(x)

        def increment(num, num_ones): #list of integers
            #replace 1 with 0 until we find a 0
            for i in range(len(num)-1,-1,-1):
                if num[i] == "0":
                    num_ones += 1
                    num[i] = "1"
                    return num, num_ones
                else:
                    num[i] = "0"
                    num_ones -= 1
            print("probably went wrong",num,num_ones)
            return num, num_ones #shouldn't happen
        
        number = list(bin(left).replace("b","0").zfill(int(np.floor(np.log2(right)))+1))
        num_ones = number.count("1")
        total = 0


        if num_ones in primes:
            total += 1

        for i in range(right-left):
            number, num_ones = increment(number, num_ones)
            if num_ones in primes:     
                total += 1

        return total
    

solver = Solution()
left = 10
right = 15
print(solver.countPrimeSetBits(left, right))


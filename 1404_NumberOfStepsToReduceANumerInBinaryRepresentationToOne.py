class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        
        while s != "1":
            if s[-1] == "0": #half -> shift to the right
                s = s[:-1]
            elif s[-1] == "1": #add 1
                i = len(s) - 1
                while i>=0 and s[i] == "1":
                    s = s[:i]+"0"+s[i+1:]
                    i -= 1
                if i == -1:
                    s = "1" + s
                else:
                    s = s[:i]+"1"+s[i+1:]

            steps += 1

        return steps
    
s = "1111011110000011100000110001011011110010111001010111110001"
# s = "1101"
solver = Solution()
print(Solution.numSteps(solver, s))
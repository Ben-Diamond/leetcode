class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # first, make a dictionary of all binary codes of length k
        # then, use a sliding window of s to check

        queue = [""]
        for i in range(k):
            newq = []
            for code in queue:
                newq.append(code+"0")
                newq.append(code+"1")
            queue = newq.copy()

        codes = {code: False for code in queue}
        remaining = 2**k

        for start in range(len(s)-k+1):
            code = s[start:start+k]
            if codes[code] == False:
                codes[code] = True
                remaining -= 1
                if remaining == 0:
                    return True

        return False
    

solver = Solution()
s = "0110"
k = 2
print(solver.hasAllCodes(s,k))
"""
You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". 
This process repeats until no occurrences of "01" exist.
"""

class Solution:
    def secondsToRemoveOccurrences(self, s: str):
        # 01 -> 10
        time = 0

        while True:
            flag = False
            i = 0
            new = ""
            while True:
                if i < len(s) -1 and s[i] == "0" and s[i+1] == "1":
                    flag = True
                    new += "10"
                    i += 2
                else:
                    new += s[i]
                    i += 1
                if i == len(s):
                    break
            
            if not flag:
                return time

            time += 1
            s = new


solver = Solution.__new__

s = "0110101"
print(Solution.secondsToRemoveOccurrences(solver,s))


s = "11100"
print(Solution.secondsToRemoveOccurrences(solver,s))
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #if a character appears an even amount of times, we can just shove it onto any existing palindrome (including empty)
        #so the actual question is is the number of odd counts less than k
        #if more than k it can't work, since the only way to have a number appear once is to put it in the middle
        if k > len(s):
            return False
        odds = {x:False for x in "abcdefghijklmnopqrstuvwxyz"}

        for letter in s:
            odds[letter] = not odds[letter]

        count = 0
        for letter in odds:
            if odds[letter] == True:
                count += 1
        
        return count <= k

solver = Solution.__new__    
s = "leetcode"
k = 3
print(Solution.canConstruct(solver,s,k))
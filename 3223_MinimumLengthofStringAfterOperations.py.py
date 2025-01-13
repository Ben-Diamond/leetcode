class Solution:
    def minimumLength(self, s: str) -> int:
        total = 0
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        
        # remove 2 for each multiple of 2 >= 3
        for letter in letters:
            if letters[letter] >= 3:
                total += 2*((letters[letter] - 1) // 2)
                print(total)

        return len(s) - total

solver = Solution.__new__    
s = "abaacbcbb"
print(Solution.minimumLength(solver,s))
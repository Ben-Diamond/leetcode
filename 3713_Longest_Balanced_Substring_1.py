class Solution:
    
    def count_letters(self, s, length):
        letters = {}
        for i in range(length):
            if s[i] not in letters:
                letters[s[i]] = 0
            letters[s[i]] += 1
        return letters
    
    def check_balanced(self, letters, length):
        #all letters  must be the same, # unique letters * number of that letter = length
        for l in letters:
            if letters[l] * len(letters) != length:
                return False
        return True

    def longestBalanced(self, s: str) -> int:
        length = len(s)
        #start at the highest length and count down
        #keep a rolling count of every letter


        for length in range(len(s), -1, -1):
            letters = self.count_letters(s, length)
            balanced = self.check_balanced(letters, length)
            if balanced:
                return length
            for start_idx in range(1, len(s) - length + 1):
                #out with the old, in with the new
                old = s[start_idx-1]
                new = s[start_idx + length - 1]
                letters[old] -= 1
                if new not in letters:
                    letters[new] = 0
                letters[new] += 1
                if letters[old] == 0:
                    del letters[old]


                balanced = self.check_balanced(letters, length)
                if balanced:
                    return length
                
    
    

s="abbababababcbcbcbabab"
solver = Solution()
print(solver.longestBalanced(s))
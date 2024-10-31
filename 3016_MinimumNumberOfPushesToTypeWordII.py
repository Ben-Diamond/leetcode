class Solution:
    def minimumPushes(self, word: str) -> int:
        occurrances = {}
        for letter in word:
            if letter not in occurrances:
                occurrances[letter]= 0 
            occurrances[letter] += 1
        occurrances = {k: v for k, v in sorted(occurrances.items(), key=lambda item: item[1])}
        #now it is in order
        total = 0
        i = 8
        for letter in reversed(occurrances):
            total += occurrances[letter] * (i//8)
            i += 1
        return total



solver = Solution.__new__
word = "aabbccddeeffgghhiiiiii"
print(Solution.minimumPushes(solver,word))
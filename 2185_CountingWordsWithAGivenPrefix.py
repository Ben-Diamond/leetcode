class Solution:
    def prefixCount(self, words, pref: str) -> int:
        length = len(pref)
        total = 0
        for word in words:
            if word[:length] == pref:
                total += 1
        return total

solver = Solution.__new__
words = ["pay","attention","practice","attend"]
pref = "at"
print(Solution.prefixCount(solver,words,pref))
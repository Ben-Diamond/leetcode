class Solution:
    def countPrefixSuffixPairs(self, words) -> int:
        total = 0
        for i,str1 in enumerate(words):
            for str2 in words[i+1:]:
                if len(str2) >= len(str1) and str2[:len(str1)] == str1 and str2[-len(str1):] == str1:
                    total +=1
        return total

solver = Solution.__new__
words = ["a","aba","ababa","aa"]
print(Solution.countPrefixSuffixPairs(solver,words))
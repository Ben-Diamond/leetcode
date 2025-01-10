class Solution:
    def wordSubsets(self, words1, words2):
        requirements = {l:0 for l in "abcdefghijklmnopqrstuvwxyz"}
        out = []
        for word in words2:
            counts = {}
            for letter in word:
                if letter not in counts:
                    counts[letter] = 0
                counts[letter] += 1
                if counts[letter] > requirements[letter]:
                    requirements[letter] += 1

        for word in words1:
            counts = {}
            for letter in word:
                if letter not in counts:
                    counts[letter] = 0
                counts[letter] += 1
            flag = True
            for letter in requirements:
                if requirements[letter] > 0 and (letter not in counts or requirements[letter] > counts[letter]):
                    flag = False
                    break
            if flag:
                out.append(word)
        return out
solver = Solution.__new__
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]
print(Solution.wordSubsets(solver,words1,words2))
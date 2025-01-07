class Solution:
    def stringMatching(self, words):
        out = set()
        for w1 in range(len(words)):
            for w2 in range(len(words)):
                if w1 != w2 and words[w1] in words[w2]:
                    out.add(words[w1])
        return list(out)

solver = Solution.__new__    
words = ["blue","green","bu"]
print(Solution.stringMatching(solver,words))
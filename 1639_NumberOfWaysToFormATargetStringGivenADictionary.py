#does not work on 86 or higher
class Solution:
    def numWays(self, words, target: str) -> int:
        bigNumber = int(1e9 + 7)
        #aoc day 15 type difficulty
        #the order of words is completely unimportant
        #instead, the only thing that matters is what index the letters are at
        #we must increase index by at least 1 but up to anything

        #make more efficient by storing duplicates?
        letters = []
        #set up "letters" :=
        # [ {"a":5,"b":2}, {"a":1,"b":7}]
        #means that first letters there are 5 as and 2 bs
        for i in range(len(words[0])): #equal length
            temp = {}
            for word in words:
                if word[i] not in temp:
                    temp[word[i]] = 0
                temp[word[i]] += 1
            letters.append(temp)




        results = {} #a little caching
        numbers = {}
        targetL = len(target)
        lettersL = len(letters)

        def dive(wordL, i, number):

            if (wordL,i) in results:
                return (results[(wordL,i)] * number)
            total = 0
            """ total skips we can do = len(letters) - len(target)
                number of skips we have done = i - len(word) - 1
                so number of skips left = len(letters) - len(target) - i + len(word) + 1

            e.g.
            target: aba
            word: ab, i: 1, 4 + 2 - 1 + 1 - 3 = 3 yep
            but if i was 3
            """
            if wordL == targetL:
                return number
            # if wordL > targetL:
            #     print("???")

            letter = target[wordL]
            for jump in range(1, lettersL + wordL + 1 - i - targetL):
                
                if letter in letters[i + jump]:
                    # if 
                    total += dive(wordL+1, i+jump, number * letters[i + jump][letter])

            #total PER NUMBER
            results[(wordL,i)] = total // number

            return total % bigNumber
        return dive(0,-1,1)






solver = Solution.__new__

words = ["cabbaacaaaccaabbbbaccacbabbbcb","bbcabcbcccbcacbbbaacacaaabbbac","cbabcaacbcaaabbcbaabaababbacbc","aacabbbcaaccaabbaccacabccaacca","bbabbaabcaabccbbabccaaccbabcab","bcaccbbaaccaabcbabbacaccbbcbbb","cbbcbcaaaacacabbbabacbaabbabaa","cbbbbbbcccbabbacacacacccbbccca","bcbccbccacccacaababcbcbbacbbbc","ccacaabaaabbbacacbacbaaacbcaca","bacaaaabaabccbcbbaacacccabbbcb","bcbcbcabbccabacbcbcaccacbcaaab","babbbcccbbbbbaabbbacbbaabaabcc","baaaacaaacbbaacccababbaacccbcb","babbaaabaaccaabacbbbacbcbababa","cbacacbacaaacbaaaabacbbccccaca","bcbcaccaabacaacaaaccaabbcacaaa","cccbabccaabbcbccbbabaaacbacaaa","bbbcabacbbcabcbcaaccbcacacccca","ccccbbaababacbabcaacabaccbabaa","caaabccbcaaccabbcbcaacccbcacba","cccbcaacbabaacbaaabbbbcbbbbcbb","cababbcacbabcbaababcbcabbaabba","aaaacacaaccbacacbbbbccaabcccca","cbcaaaaabacbacaccbcbcbccaabaac","bcbbccbabaccabcccacbbaacbbcbba","cccbabbbcbbabccbbabbbbcaaccaab","acccacccaabbcaccbcaaccbababacc","bcacabaacccbbcbbacabbbbbcaaaab","cacccaacbcbccbabccabbcbabbcacc","aacabbabcaacbaaacaabcabcaccaab","cccacabacbabccbccaaaaabbcacbcc","cabaacacacaaabaacaabababccbaaa","caabaccaacccbaabcacbcbbabccabc","bcbbccbbaaacbaacbccbcbababcacb","bbabbcabcbbcababbbbccabaaccbca","cacbbbccabaaaaccacbcbabaabbcba","ccbcacbabababbbcbcabbcccaccbca","acccabcacbcbbcbccaccaacbabcaab","ccacaabcbbaabaaccbabcbacaaabaa","cbabbbbcabbbbcbccabaabccaccaca","acbbbbbccabacabcbbabcaacbbaacc","baaababbcabcacbbcbabacbcbaaabc","cabbcabcbbacaaaaacbcbbcacaccac"]
target="acbaccacbbaaabbbabac"

print(Solution.numWays(solver,words,target))
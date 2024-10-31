class Solution:
    def kthDistinct(self, arr, k):
        uniques = {}
        starts = []
        for letter in arr:
            if letter not in uniques:
                uniques[letter] = True
                starts.append(letter)
            else:
                uniques[letter] = False
        #set up a 
        # letters = {"a":True,"aa":False,"aaa":True} 
        # starts = {"a","b","aa","aa"} -> the order in which things are found
        count = 0
        for letter in starts:
            if uniques[letter] == True:
                count += 1
                if count == k:
                    return letter
        return ""

solver = Solution.__new__
arr,k = ["d","b","c","b","c","a"], 2
print(Solution.kthDistinct(solver,arr,k))

arr,k = ["aaa","aa","a"], 1
print(Solution.kthDistinct(solver,arr,k))

arr,k = ["a","b","a"], 3
print(Solution.kthDistinct(solver,arr,k))
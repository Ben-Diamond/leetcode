class Solution:
    def combinationSum2(self, candidates, target: int):

        #try depth-first
        results = []
        resultSet = set()
        candidates = sorted(candidates)
        print(candidates)

        newPaths = []
        for x in range(len(candidates)):
            if candidates[x] > target:
                continue
            if candidates[x] == target:
                if (candidates[x]) not in resultSet:
                    results.append([candidates[x]])
                    resultSet.add((candidates[x]))
                continue

            newPaths.append({"indices":[x],"sum":candidates[x]})
        while newPaths != []:
            paths = newPaths.copy()
            newPaths = []
            for path in paths:
                for next in range(path["indices"][-1] + 1, len(candidates)):
                    newSum = path["sum"] + candidates[next]
                    if newSum == target:
                        answer = [candidates[x] for x in path["indices"] + [next]]
                        if tuple(answer) not in resultSet:
                            resultSet.add(tuple(answer))
                            results.append(answer)
                        # results.add(tuple(path["indices"] + [next]))
                    elif newSum > target:
                        break
                    elif candidates[path["indices"][-1]] == candidates[next] and path["indices"][-1] != next -1:
                        # print("dupe")
                        pass

                    else:
                        newPaths.append({"indices": path["indices"] + [next],"sum": newSum})

        return list(results)


solver = Solution.__new__
candidates, target = [10,1,2,7,6,1,5]*1, 8
# candidates, target = [1,1],2
print(Solution.combinationSum2(solver,candidates,target))
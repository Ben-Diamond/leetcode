"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1."""



class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        connections = {}
        info = {
            k:{
               "time":0,"prev":k,"explored":False
            }
        }

        for x in range(1,n+1):
            connections[x] = {}
            if x != k:
                info[x] = {"time":10e8,"prev":-1,"explored":False}


        for time in times:
            connections[time[0]][time[1]] = time[2]



        explored = []
        node = k
        while True:
            for destination in connections[node]:
                t = info[node]["time"] + connections[node][destination]
                if info[destination]["time"] > t: #ACTUALLY come from here
                    info[destination]["time"] = t
                    info[destination]["prev"] = node
            info[node]["explored"] = True
            node = -1
            nextTime = 10e10
            for n in info:
                if not info[n]["explored"] and info[n]["time"] < nextTime:
                    node = n
                    nextTime = info[n]["time"]
            if node == -1:
                highest=-1
                for n in info:
                    if info[n]["time"] == 10e8:
                        return -1
                    if info[n]["time"] > highest:
                        highest = info[n]["time"]

                return highest
        print(info)
            

times = [[2,1,1],[2,3,1],[3,4,1]]
# times=[[1,2,1]]
n = 4
k = 2
solver = Solution.__new__
print(Solution.networkDelayTime(solver,times,4,2))


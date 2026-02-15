class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        m = n //2
        if n == 1:
            return 0

        # 1001
        
        # calculate how easy for the left, or the right

        left = s[:m]
        right = s[n%2 + m:]
        # does NOT include middle
        #calculate lowest points for left or right to reach 0 or 1
        lowest = [[0,0],[0,0]]

        for goal in ("0","1"):

            # left
            cost = 0
            if left[-1] != goal:
                cost += len(left)
            for i in range(len(left)-2,-1,-1):
                if left[i] != left[i+1]:
                    cost += i+1
            lowest[0][int(goal)] = cost

            # right (actually identical)
            cost = 0
            if right[0] != goal:
                cost += len(right)
            for i in range(1,len(right)):
                if right[i] != right[i-1]:
                    cost += len(right)-i
            lowest[1][int(goal)] = cost

        print(lowest)
        print(left,right, s)
        if n%2 == 0:
            return min(lowest[0][0]+lowest[1][0], lowest[0][1] + lowest[1][1])
        # for goal in (0,1):
        else:
            # if we do not switch the middle again
            if s[m] == "0":
                no_flip = lowest[0][0] + lowest[1][0]
                flip_left = m+1 + lowest[0][0] + lowest[1][1] # m becomes 1!!
                flip_right = m+1 + lowest[0][1] + lowest[1][0] 
            else:
                no_flip = lowest[0][1] + lowest[1][1]
                flip_left = m+1 + lowest[0][1] + lowest[1][0] # m becomes 0!!
                flip_right = m+1 + lowest[0][0] + lowest[1][1] 
            return min(no_flip, flip_left, flip_right)
            
            



    #every bit flip costs 1
    #
    # 1,1,0
    # 0,0,0
    # want to minimise total flips so just do from the left and from the right until midpoint
    # only four options: make 1 and use middle as left, make 1 and use middle as right, make 0 and use middle as left, make 0 and use middle as right



s = "00"
solver = Solution()
print(solver.minimumCost(s))
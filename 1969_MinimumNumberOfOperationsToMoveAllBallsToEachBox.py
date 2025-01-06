class Solution:
    def minOperations(self, boxes: str):
        ones = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ones.append(i)
        out = []
        for i in range(len(boxes)):
            moves = 0
            for box in ones:
                moves += abs(box - i)
            out.append(moves)

        return out

solver = Solution.__new__
boxes = "110"
print(Solution.minOperations(solver,boxes))
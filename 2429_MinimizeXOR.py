class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #num2 same number of "set bits" as x: means same number of 1s
        num1 = bin(num1)
        num2 = bin(num2)
        num1setleft = num1.count("1")
        num2setleft = num2.count("1")
        size = max(len(num1),len(num2))
        num1 = num1.zfill(size).replace("b","0")
        num2 = num2.zfill(size).replace("b","0")
        print(num1setleft,num2setleft,num1,num2)

        x = ""
        if num1setleft > num2setleft:
            #we can only make a few 1s so do it in descending order
            for i in range(size):
                if num1[i] == "1" and num2setleft > 0:
                    num2setleft -= 1
                    x += "1"
                else:
                    x += "0"
            return int(x,2)
        else:
            #we have too many 1s so fill all spares in early
            for i in range(size-1,-1,-1):
                if num1[i] == "1":
                    num2setleft -= 1
                    num1setleft -= 1
                    x += "1"
                elif num1[i] == "0" and num2setleft > num1setleft:
                    num2setleft -= 1
                    x += "1"
                else:
                    x += "0"
            return int(x[::-1],2)


num1 = 25
num2 = 72

solver = Solution.__new__
print(Solution.minimizeXor(solver,num1,num2))
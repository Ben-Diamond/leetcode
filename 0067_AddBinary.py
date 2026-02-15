class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # not going to cheat with conversion

        out = ""
        carry = 0
        i = 0
        to_int = {"0":0, "1":1}
        to_str = ("0","1")

        while True:
            i += 1
            if i > len(a):
                if i > len(b):
                    if carry:
                        return "1" + out
                    return out
                
                d1 = 0
                d2 = to_int[b[-i]]
            
            elif i > len(b):
                d1 = to_int[a[-i]]
                d2 = 0
            
            else:
                d1 = to_int[a[-i]]
                d2 = to_int[b[-i]]

            out = to_str[(d1 + d2 + carry)%2] + out
            carry = (d1 + d2 + carry)//2


solver = Solution()
a = "1010"
b = "1011"
print(solver.addBinary(a,b))
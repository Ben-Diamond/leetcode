"""
Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

No and!!!
up to 2 billion
"""




class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        digits = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
                  "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        doubles = ["","","Twen","Thir","For","Fif","Six","Seven","Eigh","Nine"]
        def recursive(num):

            if num < 20:
                return digits[num]
            if num < 100:
                return doubles[num//10] + "ty " + recursive(num%10)
            if num < 1000:
                return digits[num//100] + " Hundred " + recursive(num%100)
            if num < 1000000:
                return recursive(num//1000) + " Thousand " + recursive(num%1000)
            if num < 1000000000:
                return recursive(num//1000000) + " Million " + recursive(num%1000000)
            return recursive(num//1000000000) + " Billion " + recursive(num%1000000000)
        return recursive(num).strip().replace("  "," ")

solver = Solution.__new__
num = 2**31
print(Solution.numberToWords(solver,num))
exit()
num = 123
print(Solution.numberToWords(solver,num))
num = 12345
print(Solution.numberToWords(solver,num))
num = 1234567
Solution.numberToWords(solver,num)
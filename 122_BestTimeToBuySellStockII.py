class Solution:
    def maxProfit(self, prices) -> int:
        #buy when its about to go up
        #and sell if its about to go down
        holding = False
        money = 0
        for i in range(len(prices)-1):
            #make exception near the end

            if prices[i] >= prices[i+1] and holding:
                print("sell",i+1)
                #sell
                holding = False
                money += prices[i]
            elif prices[i] < prices[i+1] and not holding:
                print("buy",i+1)
                #buy
                holding = True
                money -= prices[i]
        if holding:
            money += prices[-1]
        return money
    

prices =[1,2,3,4,5]

solver= Solution.__new__
print(Solution.maxProfit(solver,prices))
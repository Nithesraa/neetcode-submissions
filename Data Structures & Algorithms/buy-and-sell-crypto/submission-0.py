class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for num in prices:
            if num < minprice:
                minprice = num
            else:
                maxprofit = max(maxprofit,num-minprice)
        return maxprofit 
       
#neetcode solution linear time complexity
class Solution:
  def maxProfit(self,prices:list[int])->int:
    l,r=0,1 # left = buy , right= sell
    maxP=0
    
    while r<len(prices):
      if prices[l]<prices[r]:
         profit=prices[r]-prices[l]
         maxP=max(maxP, profit)
      else:
        l=r
      r+=1
    return maxP
  

# much better ?

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit


sol=Solution()
prices = [7,1,5,3,6,4]  
print(sol.maxProfit(prices))
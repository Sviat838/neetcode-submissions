class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) == 1:
            return 0

        earn = 0

        for i in range(len(prices)):
            for y in range(i+1, len(prices)):
                earn = max(earn, prices[y]-prices[i])
            


        return earn
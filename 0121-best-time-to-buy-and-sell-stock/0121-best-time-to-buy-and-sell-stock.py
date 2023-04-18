class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 10000
        maxx = 0
        for i in range(len(prices)):
            maxx = max(maxx, prices[i] - minn)
            minn = min(minn, prices[i])
        return maxx
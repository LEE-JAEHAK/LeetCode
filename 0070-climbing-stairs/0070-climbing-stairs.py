class Solution(object):
    def climbStairs(self, n):
        dp = [1,2]*45
        if n==1: return 1
        if n==2: return 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        """
        :type n: int
        :rtype: int
        """
        
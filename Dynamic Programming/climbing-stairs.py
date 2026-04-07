class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n)]
        def recurs(n:int):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n-1] != -1:
                return dp[n-1]
            dp[n-1] =  recurs(n-1) + recurs(n-2)
            return dp[n-1]
        return recurs(n)
#https://leetcode.com/problems/climbing-stairs/description/
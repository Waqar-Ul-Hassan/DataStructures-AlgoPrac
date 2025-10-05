class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp1, dp2 = 1, 1
        for i in range(2, n+1):
            dp3 = dp2 + dp1
            dp1, dp2 = dp3, dp1
        return dp1
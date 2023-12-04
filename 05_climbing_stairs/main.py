class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        # base
        dp[0] = 1
        dp[1] = 2
        # iteration
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]
    
if __name__ == "__main__":
    s = Solution()
    n = 10
    print(s.climbStairs(n))
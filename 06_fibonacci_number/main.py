class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 1
        prev = 0
        for i in range(n-1):
            temp = ans
            ans = ans + prev
            prev = temp
        
        return ans
    
if __name__ == "__main__":
    s = Solution()
    n = 100
    print(s.fib(n))
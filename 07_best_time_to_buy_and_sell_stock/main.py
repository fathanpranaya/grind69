class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # two ptr
        ptr_buy = 0
        ptr_sell = 1
        max_profit = 0
        while ptr_sell < len(prices):
            curr_profit = prices[ptr_sell] - prices[ptr_buy]
            if prices[ptr_buy] < prices[ptr_sell]:
                max_profit = max(max_profit, curr_profit)
            else:
                ptr_buy = ptr_sell
            ptr_sell += 1

        print(prices)
        print("buy:",prices[ptr_buy])
        print("sell:",max_profit+prices[ptr_buy])
        return max_profit

if __name__ == "__main__":
    s = Solution()
    l = [7,1,5,3,6,4]
    print("Profit:",s.maxProfit(l))
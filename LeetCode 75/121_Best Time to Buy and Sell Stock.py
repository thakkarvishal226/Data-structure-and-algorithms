class Solution:
    def maxProfit(self, prices) -> int:
        left = 0
        right = 0
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left]  < prices[right]:
                max_profit = max(max_profit,current_profit)
            else:
                left = right
            right+=1
        return max_profit
            


if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    #prices = [2,4,1]
    print(s.maxProfit(prices))
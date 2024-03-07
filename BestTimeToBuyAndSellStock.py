from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # sliding window where we keep the minimum value so far and the profit we change based on current value and minimum
        minimum = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
            elif prices[i] - minimum > profit:
                profit = prices[i] - minimum

        return profit
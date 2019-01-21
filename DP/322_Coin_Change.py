class Solution:
    def coinChange(self, coins, money):
        """
        :type coins: List[int]
        :type money: int
        :rtype: int
        """
        min_coins = [0] * (money+1)
        for m in range(1, money+1):
            min_coins[m] = 10**9
            for coin in coins:
                if m >= coin:
                    min_coins[m] = min(min_coins[m-coin]+1, min_coins[m])
        r = min_coins[money]
        return r if r < 10**9 else -1

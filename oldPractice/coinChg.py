class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        if amount == 0: return 1
        if not coins: return 0
        matrix = [[0] * (amount + 1) for _ in range(len(coins))]
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                matrix[0][j] = 1
        for i in range(len(coins)):
            matrix[i][0] = 1

        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                if j < coins[i]:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - coins[i]]
        return matrix[-1][-1]

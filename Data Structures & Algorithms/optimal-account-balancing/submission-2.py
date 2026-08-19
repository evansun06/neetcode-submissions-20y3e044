from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        balances = defaultdict(int)

        for payer, payee, amount in transactions:
            balances[payer] -= amount
            balances[payee] += amount

        debt = []

        for person in balances:
            if balances[person] != 0:
                debt.append(balances[person])

        def dfs(start):

            # Skip everyone already settled
            while start < len(debt) and debt[start] == 0:
                start += 1

            # Everyone settled
            if start == len(debt):
                return 0

            minimum = float("inf")

            # Try settling debt[start] against every opposite-sign balance
            for i in range(start + 1, len(debt)):

                if debt[start] * debt[i] < 0:

                    original = debt[i]

                    # debt[start] is transferred into debt[i]
                    debt[i] += debt[start]

                    minimum = min(
                        minimum,
                        1 + dfs(start + 1)
                    )

                    # backtrack
                    debt[i] = original

            return minimum

        return dfs(0)
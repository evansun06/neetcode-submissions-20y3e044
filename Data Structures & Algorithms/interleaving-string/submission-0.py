class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            state (i, j) -> i represents the # of splits for s1, j represents the # of splits for s2

            aaaa bbbb aabbaa

                                l-2

                [True , False , False, False, False]
                [True , False, False, False, False]
        l-1     [False, False, False, False, False]
                [False, False, False, False, False]
                [False, False, False, False, False]

        """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for l1 in range(len(s1) + 1):
            for l2 in range(len(s2) + 1):

                if l1 > 0:
                    dp[l1][l2] |= (
                        dp[l1 - 1][l2]
                        and s1[l1 - 1] == s3[l1 + l2 - 1]
                    )
                if l2 > 0:
                    dp[l1][l2] |= (
                        dp[l1][l2 - 1]
                        and s2[l2 - 1] == s3[l1 + l2 - 1]
                    )
                
        return dp[len(s1)][len(s2)]
                
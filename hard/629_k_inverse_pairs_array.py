# Not my solution !!!

# Let dp[i][j] be number of permutation of numbers [1, ..., i], such that it
# has exactly j inverses. Then we can show, that:

# dp[i][j] = dp[i-1][j] + dp[i-1][j-1]+ ... + dp[i-1][j-i+1], because we can
# insert number i in i different places. Note that if j-i+1 < 0, than we need
# to stop at dp[i-1][0]. Let as also introduce cumulative sums sp[i][j] =
# dp[i][0] + ... + dp[i][j], then we can do updates in O(1). Note also starting
# values dp[i][0] = 1, because there is exactly one permutation: constant
# permutation with zero inverses. Also sp[i][0] = 1. It does not matter what we
# put in other cells, because we are going to change them, so we fill
# everything with 1.

# Complexity We have O(nk) time and space complexity.

class Solution:
    def kInversePairs(self, n, k):
        dp = [[1] * (k+1) for _ in range(n+1)]
        sp = [[1] * (k+1) for _ in range(n+1)]
        N = 10**9 + 7

        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = sp[i-1][j] if j < i else (sp[i-1][j] - sp[i-1][j-i]) % N
                sp[i][j] = (sp[i][j-1] + dp[i][j]) % N
        
        return dp[-1][-1]

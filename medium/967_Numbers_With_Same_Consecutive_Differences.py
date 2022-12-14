# Return all non-negative integers of length n such that the absolute
# difference between every two consecutive digits is k.
#
# Note that every number in the answer must not have leading zeros. For
# example, 01 has one leading zero and is invalid.
#
# You may return the answer in any order.

from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        if N == 1:
            return [i for i in range(10)]

        ans = []

        def DFS(N, num):
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N - 1, new_num)

        for num in range(1, 10):
            DFS(N - 1, num)

        return list(ans)

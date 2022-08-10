# Given two integers num and k, consider a set of positive integers with the
# following properties:
#
# The units digit of each integer is k. The sum of the integers is num. Return
# the minimum possible size of such a set, or -1 if no such set exists.
#
# Note:
#
# The set can contain multiple instances of the same integer, and the sum of an
# empty set is considered 0. The units digit of a number is the rightmost digit
# of the number.

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10 == 0 else -1
        i = 1
        res = num - k*i
        while res > 0 and res % 10 != 0:
            i+=1
            res -= k
        if res<0:
            return -1
        else:
            return i

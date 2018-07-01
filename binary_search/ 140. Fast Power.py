"""
140. Fast Power
Calculate the an % b where a, b and n are all 32bit integers.

Example
For 231 % 3 = 2

For 1001000 % 1000 = 0

Challenge
O(logn)
"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        res =  1
        while n > 0:
            if n % 2 == 1:
                res = res * a % b
            a = a ** 2 % b
            n = n // 2
        return res % b
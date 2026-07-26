class Solution(object):
    def isPowerOfFour(self, n):
        while n > 0 and n % 4 == 0:
            n //= 4

        return n == 1
        
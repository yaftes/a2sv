class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        l = 0
        while 4 ** l <= n:
            if 4 ** l == n:
                return True
            l += 1
        return False
        
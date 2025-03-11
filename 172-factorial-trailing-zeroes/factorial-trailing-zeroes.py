class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        val = 1
        for i in range(1,n + 1):
            val *= i
            
        count = 0
        while val % 10 == 0 and val != 0:
            count += 1
            val //= 10
        return count
        
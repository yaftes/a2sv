class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tot = 0
        ans = 0
        for char in s:
            if char == 'L':
                tot -= 1
            else:
                tot += 1
            if tot == 0:
                ans += 1
        return ans

        
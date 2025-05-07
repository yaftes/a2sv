class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def is_zero(k):
            diff = [0] * (n + 2)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < len(diff):
                    diff[r + 1] -= val

            dec = 0
            for i in range(n):
                dec += diff[i]
                if nums[i] > dec:
                    return False
            return True

        low, high, ans = 0, len(queries), -1
        while low <= high:
            mid = (low + high) // 2
            if is_zero(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

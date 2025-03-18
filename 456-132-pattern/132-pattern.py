class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = []
        k = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < k:
                return True
            while s and s[-1] < nums[i]:
                k = s.pop()
            s.append(nums[i])

        return False
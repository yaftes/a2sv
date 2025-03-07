class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        right_max = []
        max_ = float('-inf')
        for num in reversed(nums):
            max_ = max(max_,num)
            right_max.append(max_)
        right_max.reverse()
    
        left = 0
        l = 0
        for right in range(len(nums)):
            while left <= right and right_max[right] < nums[left]:
                left += 1
            l = max(l,right - left)
        return l
                    
        
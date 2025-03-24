class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                ans[0] = mid
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                ans[1] = mid
            if target >= nums[mid]:
                left = mid + 1                
            else:
                right = mid - 1
        return ans
                

        
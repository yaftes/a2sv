
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_length = len(nums)
        answer = [1] * num_length
        left = 1
        for i in range(num_length):
            answer[i] = left
            left *= nums[i]
        right = 1
        
        for i in range(num_length - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        for ele in nums:
            val = val ^ ele
        for i in range(len(nums)+1):
            val = val ^ i
        return val
        
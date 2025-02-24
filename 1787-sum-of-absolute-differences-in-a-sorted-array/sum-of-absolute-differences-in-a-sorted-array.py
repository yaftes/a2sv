class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        result = [0] * n
        totalSum = prefixSum[n]

        for i in range(n):
            left_sum = i * nums[i] - prefixSum[i] 
            right_sum = (totalSum - prefixSum[i + 1]) - (n - i - 1) * nums[i]
            result[i] = left_sum + right_sum

        return result




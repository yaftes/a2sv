class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # find for both maximum positive and maximum negative
        max_ = float('-inf')
        curr = 0
        for num in nums:
            curr = max(curr + num,num)
            max_ = max(curr,max_)
        print(max_)
        curr = 0
        for num in nums:
            curr = min(curr + num,num)
            max_ = max(max_,abs(curr))
        return max_

        
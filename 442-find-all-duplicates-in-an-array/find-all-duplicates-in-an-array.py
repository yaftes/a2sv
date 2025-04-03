class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        while i < len(nums):
            position = nums[i] - 1
            if position != i:
                if nums[position] == nums[i]:
                    ans.add(nums[position])
                    i += 1
                else:
                    nums[position],nums[i] = nums[i],nums[position]
            else:
                i += 1
        return list(ans)
        
        
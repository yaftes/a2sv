class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = set()
        ans = []
        for ele in nums:
            if ele in unique:
                ans.append(ele)
            else:
                unique.add(ele)
        return ans
        
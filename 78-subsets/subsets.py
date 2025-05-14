class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = 2 ** len(nums)
        for i in range(l):
            temp = []
            for j in range(32):
                if i & (1 << j) != 0:
                    temp.append(nums[j])
            ans.append(temp)
        return ans



        
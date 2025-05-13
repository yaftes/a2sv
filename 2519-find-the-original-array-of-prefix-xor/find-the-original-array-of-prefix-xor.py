class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        prev = 0 
        for num in pref:
            ans.append(prev ^ num)
            prev = num
        return ans
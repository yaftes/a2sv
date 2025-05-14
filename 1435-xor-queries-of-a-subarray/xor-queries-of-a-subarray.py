class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = []
        ele = 0
        for num in arr:
            ele ^= num
            prefix_xor.append(ele)

        ans = []
  
        for l,r in queries:
            val = prefix_xor[r] if l == 0 else prefix_xor[r] ^ prefix_xor[l - 1]
            ans.append(val)
        return ans
        
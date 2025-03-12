class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.findbin(n)
        return ans[k - 1] 

    def findbin(self, n):
        if n == 1:
            return "0"
        ans = "".join(reversed(self.invert(self.findbin(n-1))))
        return self.findbin(n - 1) + "1" + ans

    def invert(self, s):
        val = list(s)
        for i in range(len(val)): 
            if val[i] == '1':
                val[i] = '0'
            else:
                val[i] = '1'
        return "".join(val)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans.append(stack[-1] - i)
            else:
                ans.append(0)
            stack.append(i)
        ans.reverse()
        return ans
            

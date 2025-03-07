class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idx = deque()
        ans = []
        left = right = 0
        while right < len(nums):
            while idx and nums[right] > nums[idx[-1]]:
                idx.pop()
            idx.append(right)
            if right - left + 1 == k:
                ans.append(nums[idx[0]])
                if left == idx[0]:
                    idx.popleft()
                left += 1
            right += 1
        return ans
                

        
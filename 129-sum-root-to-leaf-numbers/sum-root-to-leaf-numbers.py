# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # root to leaf sum
        total_sum = 0
        
        def findSum(node,curr_sum):
            nonlocal total_sum
            if not node:
                return 
            curr_sum = curr_sum * 10 + node.val
            if node.left is None and node.right is None:
                total_sum += curr_sum
                return 
            findSum(node.left,curr_sum)
            findSum(node.right,curr_sum)
            
        findSum(root,0)
        return total_sum



        
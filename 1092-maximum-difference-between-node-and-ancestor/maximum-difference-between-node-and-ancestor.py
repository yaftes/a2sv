# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = []
        if not root:
            return 0
        def findMax(node,max_,min_):
            if not node:
                return
            min_ = min(min_,node.val)
            max_ = max(max_,node.val)
            ans.append(max_ - min_)
            findMax(node.left,max_,min_)
            findMax(node.right,max_,min_)
        
        val = findMax(root,root.val,root.val)
        return max(ans)

            
        
        

        
        
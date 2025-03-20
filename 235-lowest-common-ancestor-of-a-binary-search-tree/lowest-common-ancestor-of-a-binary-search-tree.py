# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if current node left and right value is qual p and q
        def finder(node):
            if not node:
                return
            minm_ = min(p.val,q.val)
            maxm_ = max(p.val,q.val)
            if node.val == minm_ or node.val == maxm_:
                return node
            elif node.val > minm_ and node.val < maxm_:
                return node
            elif node.val > maxm_:
                return finder(node.left)
            else:
                return finder(node.right)
        node = finder(root)
        return node


        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new_node = TreeNode(val)
            root = new_node
            return root

        def finder(node):
            if node.val > val and node.left is None:
                new_node = TreeNode(val)
                node.left = new_node
                return
            elif node.val < val and node.right is None:
                new_node = TreeNode(val)
                node.right = new_node
                return
            elif node.val < val:
                finder(node.right)
            else:
                finder(node.left)
        finder(root)
        return root



       

        
        
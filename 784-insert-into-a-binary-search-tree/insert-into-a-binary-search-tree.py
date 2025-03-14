# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            new_node = TreeNode(val)
            root = new_node
            return root
        def finder(root):
            if root.left is None and root.val > val:
                new_node = TreeNode(val)
                root.left = new_node
                return root
            elif root.right is None and root.val < val:
                new_node = TreeNode(val)
                root.right = new_node
                return root
            elif root.val > val:
                return self.insertIntoBST(root.left,val)
            else:
                return self.insertIntoBST(root.right,val)
        finder(root)
        return root
       

        
        
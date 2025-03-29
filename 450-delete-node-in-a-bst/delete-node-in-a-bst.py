class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            succ = self.findMin(root.right)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node



        

            



        
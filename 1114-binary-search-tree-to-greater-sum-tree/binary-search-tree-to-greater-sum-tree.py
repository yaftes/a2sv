class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.accumulated_sum = 0
        
        def dfs(node):
            if node is None:
                return 0

            dfs(node.right)
            self.accumulated_sum += node.val
            node.val = self.accumulated_sum
            dfs(node.left)

        dfs(root)
        
        return root



        
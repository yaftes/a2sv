

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        def buildBalancedTree(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = buildBalancedTree(start, mid - 1)
            node.right = buildBalancedTree(mid + 1, end)
            return node
        
        return buildBalancedTree(0, len(nodes) - 1)

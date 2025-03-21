# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def countAve(node):
            if node is None:
                return (0, 0) 

            sumLeft, countLeft = countAve(node.left)
            sumRight, countRight  = countAve(node.right)

            Sum = sumLeft + sumRight + node.val
            nodeCount = countLeft + countRight + 1

            if Sum//nodeCount == node.val:
                self.count += 1
                
            return (Sum, nodeCount)

        countAve(root)
        return self.count

            
        
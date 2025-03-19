# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        hm = defaultdict(list)
        def findOddNodes(node,row_no):
            if node is None:
                return
            if row_no % 2 == 1:
                hm[row_no - 1].append(node.val)
            findOddNodes(node.left,row_no + 1)
            findOddNodes(node.right,row_no + 1)
        findOddNodes(root,0)

        def changeValues(node,row_no):
            if node is None:
                return
            if row_no in hm:
                node.left.val = hm[row_no].pop()
                node.right.val = hm[row_no].pop()
            changeValues(node.left,row_no + 1)
            changeValues(node.right,row_no + 1)
            
        changeValues(root,0)
    
        return root

        
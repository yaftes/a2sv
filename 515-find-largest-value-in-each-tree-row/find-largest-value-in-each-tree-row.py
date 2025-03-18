# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        hm = defaultdict(list)
        if root:
            hm[0] = [root.val]

        def findMax(node,row_no):
            if node is None:
                return
            if node.left:
                hm[row_no].append(node.left.val)
            if node.right:
                hm[row_no].append(node.right.val)
            row_no += 1
            findMax(node.left,row_no)
            findMax(node.right,row_no)
        findMax(root,1)

        ans = []
        for ele in hm:
            ans.append(max(hm[ele]))
       
        return ans


        
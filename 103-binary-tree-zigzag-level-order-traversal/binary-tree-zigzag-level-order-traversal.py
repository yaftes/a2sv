# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hm = defaultdict(list)
        def findZigZag(node,row_num):
            if node is None:
                return
            hm[row_num].append(node.val)
            findZigZag(node.left,row_num + 1)
            findZigZag(node.right,row_num + 1)

        findZigZag(root,1)

        ans = []
        for key in hm:
            if key % 2 == 0:
                hm[key].reverse()
            ans.append(hm[key])
        return ans

        


        
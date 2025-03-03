# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = self.findlength(head) // 2
        stack = []
        curr = head
        max_ = 0
        while curr:
            if length <= 0  and stack:
                max_ = max(stack.pop() + curr.val,max_)
            else:
                stack.append(curr.val)
                length -= 1
            curr = curr.next
        return max_

    def findlength(self,head):
        curr = head
        c = 0
        while curr:
            c += 1
            curr = curr.next
        return c
        
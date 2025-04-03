# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
   

        def mergeSort(node):
            if node is None or node.next is None:
                return node
            middle = self.getMiddle(node)
            left = node
            right = middle.next
            middle.next = None
            left_arr = mergeSort(left) 
            right_arr = mergeSort(right) 
            return self.merge(left_arr, right_arr)

        if not head: 
          return None

        return mergeSort(head)

    def getMiddle(self, head): 
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next
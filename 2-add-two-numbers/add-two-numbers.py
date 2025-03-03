# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        temp = 0
        curr1 = l1
        curr2 = l2
        while curr1 and curr2:
            new_node = ListNode()
            value = curr1.val + curr2.val + temp
            if value > 9:
                new_node.val = value % 10
                temp = value // 10
            else:
                new_node.val = value
                temp = 0
            head.next = new_node
            head = new_node
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr2:
            new_node = ListNode()
            value = curr2.val + temp
            if value > 9:
                new_node.val = value % 10
                temp = value // 10
            else:
                new_node.val = value
                temp = 0
            head.next = new_node
            head = new_node
            curr2 = curr2.next
            
        while curr1:
            new_node = ListNode()
            value = curr1.val + temp
            if value > 9:
                new_node.val = value % 10
                temp = value // 10
            else:
                new_node.val = value
                temp = 0
            head.next = new_node
            head = new_node
            curr1 = curr1.next
        if temp > 0:
            new_node = ListNode()
            new_node.val = temp
            head.next = new_node

        return ans.next
        
                
        

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        def reverse(h, count):
            prev, curr = None, h
            while count > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count -= 1
            return prev, curr

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while True:
            cur = pre.next
            cnt = 0
            temp = cur
            while temp and cnt < k:
                temp = temp.next
                cnt += 1

            if cnt < k:
                break

            rev_head, nxt_head = reverse(cur, k)

            pre.next = rev_head
            cur.next = nxt_head

            pre = cur

        return dummy.next
            
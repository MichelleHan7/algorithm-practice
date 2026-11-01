# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        p = dummy = ListNode(next=head)
        pre = None
        cur = head
        while count >= k:
            count -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p.next
            p.next = pre
            nxt.next = cur
            p = nxt
        return dummy.next

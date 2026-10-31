"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0, next=head)
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = dummy
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
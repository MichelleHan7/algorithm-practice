# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        first = self.mergeKLists(lists[:n//2])
        second = self.mergeKLists(lists[n//2:])
        return self.mergeTwoLists(first, second)
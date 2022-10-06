# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        if head is None or head.next is None and n == 1 : return None
        for i in range(n):
            if fast.next is None:
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow.next is not None:
            slow.next = slow.next.next
        return head

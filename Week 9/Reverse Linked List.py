class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev

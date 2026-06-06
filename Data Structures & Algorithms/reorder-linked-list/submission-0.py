class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        
        prev = None
        cur = middle
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        first, second = head, prev
        while second:
            next1 = first.next
            next2 = second.next
            
            first.next = second
            second.next = next1
            
            first = next1
            second = next2
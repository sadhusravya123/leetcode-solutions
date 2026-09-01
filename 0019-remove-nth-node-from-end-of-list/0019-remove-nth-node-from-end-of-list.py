class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy= ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy
        for _ in range(n):
            first=first.next
        while first.next:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy.next        
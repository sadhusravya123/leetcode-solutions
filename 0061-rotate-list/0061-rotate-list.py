class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        k = k % n
        curr = head
        while curr.next:
            curr = curr.next

        curr.next = head
        for _ in range(n - k):
            curr = curr.next

        head = curr.next
        curr.next = None

        return head
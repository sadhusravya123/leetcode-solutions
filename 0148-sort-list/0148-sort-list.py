class Solution(object):
    def sortList(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        dummy = ListNode(0)
        curr = dummy

        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next
        
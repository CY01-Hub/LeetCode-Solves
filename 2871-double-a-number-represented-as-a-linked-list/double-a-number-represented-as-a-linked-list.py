# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            agla = curr.next
            curr.next = prev
            prev = curr
            curr = agla

        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)

        curr = head
        carry = 0

        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10
            curr = curr.next

        head = self.reverse(head)

        if carry:
            head = ListNode(carry, head)

        return head
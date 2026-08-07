# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # 2. Advance fast pointer by n steps
        for _ in range(n):
            fast = fast.next

        # 3. Move both pointers together until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # 4. Skip the target node
        slow.next = slow.next.next

        # 5. Return the updated head (dummy.next handles head deletion automatically)
        return dummy.next
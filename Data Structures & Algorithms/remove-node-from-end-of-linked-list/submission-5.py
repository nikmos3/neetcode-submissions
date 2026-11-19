# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        count = 0

        curr = head

        while curr:
            count += 1
            curr = curr.next

        nth_node = count - n
        if nth_node == 0:
            return head.next

        curr = head
        i = 1
        while curr:
            if i == nth_node:
                curr.next = curr.next.next
                return head
                    

            i += 1
            curr = curr.next

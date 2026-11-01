# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prevg = dummy
        while True:
            kth = self.kthlist(prevg,k)
            if not kth:
                break
            prevn = kth.next
            
            prev, curr = kth.next, prevg.next
            while curr != prevn:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = prevg.next
            prevg.next = kth
            prevg = temp
        return dummy.next
                


    def kthlist(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr

        
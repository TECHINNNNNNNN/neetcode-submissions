# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return

        if head.next == None:
            return head
        
        if head.next.next == None:
            curr = head.next
            prev = head
            curr.next = prev
            head.next = None
            return curr

        prev = head
        curr = head.next
        nex = head.next.next

        head.next = None
        while nex != None:
            curr.next = prev
            prev = curr
            curr = nex
            nex = nex.next
        

        
        curr.next = prev

        return curr





        


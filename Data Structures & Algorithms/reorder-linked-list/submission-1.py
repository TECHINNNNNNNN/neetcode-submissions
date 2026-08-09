# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            mid = mid.next
        

        cur = mid.next
        mid.next = None
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        begin = head

        while prev:
            tmp = begin.next
            tmp_2 = prev.next
            begin.next = prev
            prev.next = tmp
            begin = tmp
            prev = tmp_2

        
        

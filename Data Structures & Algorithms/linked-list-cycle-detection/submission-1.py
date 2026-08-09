# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        node = set()
        lastnode = head
        node.add(lastnode)

        while lastnode.next and lastnode.next not in node:
            lastnode = lastnode.next
            node.add(lastnode)
        
        if lastnode.next != None:
            return True
        
        return False
        
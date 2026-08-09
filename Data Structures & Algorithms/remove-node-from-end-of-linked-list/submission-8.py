# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return None
        left = ListNode(None,head)
        
        link_length = 1
        cur = head
        while cur.next:
            cur = cur.next
            link_length += 1

        print(f"link_length {link_length}")
        pos_to_delete = link_length - (n - 1)
        print(f"pos_to_delete {pos_to_delete}")

        before = left
        for i in range(pos_to_delete - 1):
            before = before.next
        
        after = left
        for i in range(pos_to_delete + 1):
            after = after.next
            print("action")
        
        print(f"before {before.val}")
        if pos_to_delete == 1:
            left.next = after
            return after
    

        
        before.next = after
        return head
        

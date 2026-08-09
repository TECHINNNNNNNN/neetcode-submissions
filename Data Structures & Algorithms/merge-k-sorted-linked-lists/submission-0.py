# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = None
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0,len(lists), 2):
                if i + 1 >= len(lists):
                    merged_list.append(lists[i])
                else:
                    merged_head = self.mergeTwoLists(lists[i],lists[i+1])
                    merged_list.append(merged_head)
            lists = merged_list

        
        return lists[0]
        
    

    def mergeTwoLists(self,list1,list2):
        dummy = ListNode(-1)
        tail = dummy
    
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next
            else :
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
        
        if cur1:
            tail.next = cur1

        
        if cur2:
            tail.next = cur2

        
        return dummy.next
            


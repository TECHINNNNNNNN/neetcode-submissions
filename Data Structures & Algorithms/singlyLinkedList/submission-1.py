
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head.next == None:
            self.tail = newNode
        newNode.next = self.head.next
        self.head.next = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        cur = self.head.next
        prev = self.head
        i = 0
        while cur:
            nxt = cur.next
            temp_cur = cur
            if i == index:
                if cur.next == None:
                    self.tail = prev
                prev.next = cur.next
                cur.next = None
                return True
            cur = nxt
            prev = temp_cur
            i += 1
        return False


        

    def getValues(self) -> List[int]:
        result = []
        cur = self.head.next
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
        

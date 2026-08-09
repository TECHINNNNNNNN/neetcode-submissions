class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = self.right = None


    def isEmpty(self) -> bool:
        return self.left == None and self.right == None
        

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        currentNode = self.right
        if self.isEmpty():
            self.left = newNode
            self.right = newNode
        else:
            self.right.next = newNode
            self.right = self.right.next
            newNode.prev = currentNode
        

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            self.left = newNode
            self.right = newNode
            return
        nextValue = self.left
        newNode.next =  nextValue
        nextValue.prev = newNode
        self.left = newNode
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        elif self.left == self.right:
            popValue = self.right.val
            self.left = None
            self.right = None
            return popValue
        else:
            popValue = self.right.val
            self.right = self.right.prev
            self.right.next = None
            return popValue
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        elif self.left == self.right:
            popValue = self.left.val
            self.left = None
            self.right = None
            return popValue
        else:
            popValue = self.left.val
            newHead = self.left.next
            self.left.next = None
            self.left = newHead
            newHead.prev = None
            return popValue
        

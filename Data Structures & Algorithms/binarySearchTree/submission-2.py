class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    

class TreeMap:
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        self.root = self._insert(self.root,key,val)
    
    def _insert(self, root , key, val):
        if not root:
            return TreeNode(key, val)
        
        if key < root.key :
            root.left = self._insert(root.left,key,val)
        elif key > root.key:
            root.right = self._insert(root.right,key,val)
        elif key == root.key:
            root.key = key
            root.val = val
            return root
        return root


    def get(self, key: int) -> int:
        return self._get(self.root,key)
    
    def _get(self,root,key):
        if not root:
            return -1
        
        if key < root.key:
            return self._get(root.left,key)
        elif key > root.key:
            return self._get(root.right,key)
        else:
            return root.val


    def getMin(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr.left:
            curr = curr.left
        
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        
        return curr.val


    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)
    
    def _remove(self,root,key):
        if not root:
            return
        
        if key < root.key:
            root.left = self._remove(root.left,key)
        elif key > root.key:
            root.right = self._remove(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self._remove(root.right,root.key)
            
        return root

    
    def minValueNode(self,root):
        if not root:
            return None
        
        curr = root
        while curr.left:
            curr = curr.left
        
        return curr



    def getInorderKeys(self) -> List[int]:
        res = []
        self._getInorderKeys(self.root,res)
        return res
    
    def _getInorderKeys(self, root, res):
        if not root:
            return 
        self._getInorderKeys(root.left,res)
        res.append(root.key)
        self._getInorderKeys(root.right,res)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        if root:
            queue.append(root)
        
        result = []
        level = 0
        while queue:
            lenq = len(queue)
            for i in range(lenq):
                curr = queue.popleft()
                print("val : ", curr.val)
                print("level : ", level)
                if i == lenq - 1:
                    result.append(curr.val)
                if curr.left:
                    print("curr left", curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    print("curr right: ", curr.right.val)
                    queue.append(curr.right)
                print("result: ", result)
            level += 1
        
        return result
        
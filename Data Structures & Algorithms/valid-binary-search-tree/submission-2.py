# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
    
    def validate(self,node,min_range,max_range):
        if not node:
            return True
        
        if node.val <= min_range or node.val >= max_range:
            return False
        
        left = self.validate(node.left, min_range , node.val)
        right = self.validate(node.right,node.val ,max_range)

        return left and right

        
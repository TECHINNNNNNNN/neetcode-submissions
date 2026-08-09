# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, res):
            if root == None:
                return res
            

            max_left = helper(root.left, 1 + res)
            max_right = helper(root.right, 1 + res)


            return max(max_left,max_right)
        
        return helper(root,0)
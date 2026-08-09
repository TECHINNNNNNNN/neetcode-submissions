# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder_section,inorder_section):
            if len(preorder_section) == 0 or len(inorder_section) == 0:
                return None
            
            root = TreeNode(preorder_section[0])
            midindex = inorder_section.index(root.val)

            left_inorder_section = inorder_section[:midindex]
            right_inorder_section = inorder_section[midindex + 1:]

            left_preorder_section = preorder_section[1:1 + midindex]
            right_preorder_section = preorder_section[midindex + 1:]

            root.left = build(left_preorder_section, left_inorder_section)
            root.right = build(right_preorder_section, right_inorder_section)

            return root
        
        return build(preorder,inorder)
        

        
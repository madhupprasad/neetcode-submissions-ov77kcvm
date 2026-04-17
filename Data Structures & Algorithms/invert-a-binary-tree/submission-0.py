# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def parse(node):
            if node == None:
                return None
            
            left = parse(node.left)
            right = parse(node.right)

            node.left = right
            node.right = left

            return node
        
        return parse(root)
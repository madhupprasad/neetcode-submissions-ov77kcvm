# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def parse(node,left, right):
            if node is None:
                return True
            
            if not (left < node.val < right):
                return False
            
            return parse(node.left, left, node.val) and parse(node.right, node.val, right)

        return parse(root, -1001, 1001)
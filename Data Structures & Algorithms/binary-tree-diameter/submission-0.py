# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def parse(node):
            if node == None:
                return -1
            
            lh = parse(node.left) + 1
            rh = parse(node.right) + 1

            print(node.val, "-->",lh, rh)

            self.res = max(self.res, lh + rh)
            
            return max(lh, rh)
        
        parse(root)

        return self.res
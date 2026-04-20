# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flag = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def parse(node):
            if node == None:
                return -1
            
            lh = parse(node.left) + 1
            rh = parse(node.right) + 1

            if abs(rh - lh) > 1:
                self.flag = False

            return max(lh,rh)
        parse(root)
        return self.flag
    

            
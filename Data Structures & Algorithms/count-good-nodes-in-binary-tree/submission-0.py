# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        def parse(node, maxval):
            if not node:
                return None
            if node.val >= maxval:
                self.res+=1
            l = parse(node.left, max(node.val, maxval))
            r = parse(node.right, max(node.val, maxval))
        
        parse(root, root.val)

        return self.res
            

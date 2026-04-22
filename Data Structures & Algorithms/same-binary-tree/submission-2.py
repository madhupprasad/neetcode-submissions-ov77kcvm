# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def parse(node, a):
            if node == None:
                a.append(None)
                return None
            
            parse(node.left,a)
            print(node.val)
            parse(node.right,a)
            a.append(node.val)

        x,y = [],[]

        parse(p, x)
        parse(q, y)

        return x == y
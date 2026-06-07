# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """ initial idea - level order traversal
        last item in Q will be in right side"""
        if not root:
            return []

        q = deque([root])
        res = [root.val]
        while q:
            l = len(q)
            for i in range(l):
                v = q.popleft()
                if v.left:                
                    l = v.left
                    q.append(l)
                if v.right:
                    r = v.right
                    q.append(r)
            if q:
                res.append(q[-1].val)
        
        return res



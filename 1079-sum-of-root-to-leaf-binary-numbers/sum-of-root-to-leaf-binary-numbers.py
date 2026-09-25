# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        res=[]
        def solve(root,s):
            if not root:
                return 
            s+=str(root.val)
            if not root.left and not root.right:
                res.append(int(s,2))
                return
            solve(root.left,s)
            solve(root.right,s)
        solve(root,"")
        return sum(res)
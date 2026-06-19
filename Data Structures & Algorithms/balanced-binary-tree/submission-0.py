# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        l = self.maxh(root.left)
        r = self.maxh(root.right)
        if abs(l-r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxh(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1+max(self.maxh(node.left),self.maxh(node.right))

        
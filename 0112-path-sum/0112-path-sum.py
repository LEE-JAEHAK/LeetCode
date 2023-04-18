# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    num = 0
    def trav(self, root: Optional[TreeNode], no, targetSum):
        if root == None:
            return
        root.val += no
        if root.left == None and root.right == None:
            if targetSum == root.val:
                self.num = 1
                return
            return
        self.trav(root.left, root.val, targetSum)
        self.trav(root.right, root.val, targetSum)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.trav(root, 0, targetSum)
        if self.num == 1:
            return True
        else:
            return False
        
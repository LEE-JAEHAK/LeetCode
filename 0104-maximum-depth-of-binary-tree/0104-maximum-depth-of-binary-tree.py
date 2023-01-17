# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    maxi = 0
    def dfs(self, root, d):
        if root == None: return
        self.maxi = max(self.maxi, d)
        self.dfs(root.left, d + 1)
        self.dfs(root.right, d + 1)
        return self.maxi
        
    def maxDepth(self, root):
        if root == None: return 0
        return(self.dfs(root, 1))
        """
        :type root: TreeNode
        :rtype: int
        """
        
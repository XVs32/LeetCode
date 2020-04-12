# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        long = 0
        short = 0
        count = len(root)
        level = 0
        while count != 0:
            level += 1
            
            if count % 2 != 0:
                short = long
                long = level 
            
        return long + short - 1
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    max_level = 0
    
    def traverse(self, root, level):
        
        flag = 0
        left_level = 0
        right_level = 0
        
        if root.left != None:
            left_level = self.traverse(root.left, level + 1 )
            flag += 1
        
        if root.right != None:
            right_level = self.traverse(root.right, level + 1 )
            flag += 1
            
        if flag == 2:
            if self.max_level < left_level + right_level - (level * 2):
                self.max_level = left_level + right_level - (level * 2)
            return max(left_level, right_level)
        elif flag == 1:
            if self.max_level < max(left_level, right_level) - level:
                self.max_level = max(left_level, right_level) - level
            return max(left_level, right_level)
        elif flag == 0:
            return level
            
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        self.traverse(root, 1)
        
        return self.max_level
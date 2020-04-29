# day_11: Diameter of Binary Tree 

###### tags: `online_judge`, `python3`

給定一棵二元樹，問任意兩個節點的最長距離是多少。


最長路徑不一定會經過根節點，但一定會經過擁有左右子節點的節點（根節點除外喔）。
這是因為如果一個節點只有一個子節點，那麼只要往子節點方向走就可以得到更長的距離了（除非你走到葉子〔末端〕，無法再往下走）。
但如果擁有左右子節點，那麼就可以同時往左右走，而無視掉從父節點來的路徑。
例如：

            1
           / \
          2   3
         / \     
        4   5  
       /     \
      6       7
     /         \
    8           9 
    
最長路徑就是 8 -> 6 -> 4 -> 2 -> 5 -> 7 -> 9，並不會經過根節點。
　　　
實際操作上可以以遞迴從根節點開始遍歷，每個節點都回傳自身往下走的最長距離。而同時持有左右節點的節點和根節點則需要額外計算自身往左和往右的最長距離，這個最長距離就是題目的答案。
   
---

## 題目

```
 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 
```

---

## 解答

```python=
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
```

---
### 成績

![](https://i.imgur.com/olQPdtY.png)



---
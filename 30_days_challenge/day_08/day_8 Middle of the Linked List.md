# day_8: Middle of the Linked List

###### tags: `online_judge`, `python3`

給定一個 linked list, 回傳 linked list 的中央節點。

本題屬於 linked list 的基本操作，解法是快慢機，使用一個 step = 1 的指標，和一個 step = 2 的指標。當 step = 2 的指標指向 linked list 末端時，step = 1 的指標會正好指向 linked list 中央。

---

## 題目

```
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

 

Note:

    The number of nodes in the given list will be between 1 and 100.
```

---

## 解答

```python=
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        
        slow = ListNode(0,head)
        fast = ListNode(0,head)
        
        while True:
            slow = slow.next
            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
            else:
                break
                
        return slow

        
a = Solution()

print (a.middleNode([1,2,3]))
print (a.middleNode([1,1,3,3,5,5,7,7]))
print (a.middleNode([1,3,2,3,5,0]))
print (a.middleNode([1,1,2,2]))
print (a.middleNode([2,9,0,7,6,2,7,7,0]))
```

---
### 成績

![](https://i.imgur.com/GJwuuR7.png)



---
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



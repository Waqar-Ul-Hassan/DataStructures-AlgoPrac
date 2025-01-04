# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        res = []

        while head.next != None:
            if head in res:
                return True
            l = head
            head = head.next
            res.append(l)

        return False
    
        
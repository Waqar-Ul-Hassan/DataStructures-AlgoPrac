# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        nodesA = []
        nodesB = []

        while headA.next is not None:
            nodesA.append(headA)
            headA = headA.next

        nodesA.append(headA)

        while headB.next is not None:
            if headB in nodesA:
                return headB
            headB = headB.next

        if headB in nodesA:
                return headB
        return None
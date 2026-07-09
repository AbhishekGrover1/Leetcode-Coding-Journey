# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        # Dummy node to safely handle cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Move prev to the node right before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
            
        # curr will point to the first node of the sublist to be reversed
        curr = prev.next
        
        # Step 2: Reverse the sublist using a single pass look-ahead switch
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            
        return dummy.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head
        
        # Dummy node to safely handle the head change
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # 1. Check if there are at least k nodes left to reverse
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Fewer than k nodes left; execution is done
            
            # Keep track of the node after this k-group
            next_group_start = kth.next
            
            # 2. Reverse the k-group
            prev = next_group_start
            curr = group_prev.next
            group_head = curr  # This will become the tail of the reversed group
            
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # 3. Reconnect the reversed group back into the main list
            group_prev.next = prev
            group_prev = group_head  # Move group_prev to the end of the current group
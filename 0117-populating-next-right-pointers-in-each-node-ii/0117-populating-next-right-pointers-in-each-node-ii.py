"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        curr = root  # Tracks the head of the current level
        
        while curr:
            dummy = Node(0)  # Dummy node to construct the next level's linked list
            tail = dummy     # Tail pointer to append nodes to the next level
            
            # Traverse the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # Move to the next node in the current level
                
            # Move down to the start of the next level
            curr = dummy.next
            
        return root
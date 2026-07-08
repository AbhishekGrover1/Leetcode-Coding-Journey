class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Base Cases
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        
        # Check memoization cache
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        # Pruning: Quick check if both strings have the same character frequencies
        if sorted(s1) != sorted(s2):
            self.memo[(s1, s2)] = False
            return False
            
        n = len(s1)
        
        # Try splitting at every possible length i for the left partition
        for i in range(1, n):
            # Case 1: No Swap
            # s1_left vs s2_left AND s1_right vs s2_right
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[(s1, s2)] = True
                return True
                
            # Case 2: Swap occurred
            # s1_left vs s2_right (from end) AND s1_right vs s2_left (from start)
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                self.memo[(s1, s2)] = True
                return True
                
        self.memo[(s1, s2)] = False
        return False
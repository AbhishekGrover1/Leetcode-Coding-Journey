class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx, p_idx = 0, 0
        star_idx = -1
        s_match = 0
        
        while s_idx < len(s):
            # Case 1: Match found or '?' wildcard matches any single character
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            
            # Case 2: '*' wildcard encountered, record the checkpoint positions
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                s_match = s_idx
                p_idx += 1
            
            # Case 3: Mismatch occurs, backtrack to the last '*' checkpoint
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_match += 1
                s_idx = s_match
                
            # Case 4: Complete mismatch with no active '*' fallback
            else:
                return False
                
        # Check if remaining characters in the pattern are all '*'
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        # If the string is too short or too long, it can't form a valid IP
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start, current_path):
            # Base Case: If we have 4 segments and processed the entire string
            if len(current_path) == 4:
                if start == len(s):
                    res.append(".".join(current_path))
                return
            
            # Explore segments of length 1, 2, and 3
            for length in range(1, 4):
                # Ensure we don't go out of bounds
                if start + length > len(s):
                    break
                    
                segment = s[start : start + length]
                
                # Check for leading zeros: if length > 1, it can't start with '0'
                if segment[0] == '0' and length > 1:
                    continue
                    
                # Check value bounds
                if int(segment) <= 255:
                    # Choose and recurse
                    backtrack(start + length, current_path + [segment])
                    
        backtrack(0, [])
        return res
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        # If the total lengths don't match, it's impossible to interleave
        if len1 + len2 != len3:
            return False
            
        # dp[i][j] will store if s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Base case: empty strings interleave to form an empty string
        dp[0][0] = True
        
        # Fill the first row (matching s2 exclusively with s3)
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the first column (matching s1 exclusively with s3)
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        # Fill the rest of the dp table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # Can we match the current char of s3 with s1?
                match_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                # Can we match the current char of s3 with s2?
                match_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                
                dp[i][j] = match_s1 or match_s2
                
        return dp[len1][len2]
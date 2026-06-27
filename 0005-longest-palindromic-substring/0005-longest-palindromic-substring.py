class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""

        start, end = 0, 0

        def expand_around_centre(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1 
            # Return the lenght of the palindrome found 
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd lenght (centre is at i)
            len1 = expand_around_centre(i, i)
            # Case 2: Even lenght (centre is between i and i+1)
            len2 = expand_around_centre(i, i + 1)

            # Find the maximum of both cases 
            max_len = max(len1, len2)

            # Update the boundaries of our longest palindromic substring
            if max_len > end - start:
                start = i - (max_len - 1) // 2 
                end = i + max_len // 2 

        return s[start:end + 1]    

        
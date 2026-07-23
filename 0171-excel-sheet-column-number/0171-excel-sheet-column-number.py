class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            # Convert character to value (A -> 1, B -> 2, ..., Z -> 26)
            val = ord(char) - ord('A') + 1
            # Shift previous digits by base 26 and add the current character value
            result = result * 26 + val
            
        return result
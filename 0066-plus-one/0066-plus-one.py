class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the list in reverse order
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0
            digits[i] = 0
            
        # If all digits were 9, we need an extra 1 at the front
        return [1] + digits
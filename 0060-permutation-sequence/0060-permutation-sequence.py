import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Create a list of numbers to choose from: [1, 2, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to 0-based indexing to match list indices
        k -= 1
        
        # Precompute factorial values or use math.factorial
        # Since n <= 9, calculating it on the fly is extremely fast
        factorial = math.factorial(n - 1)
        
        result = []
        
        while n > 0:
            # Determine the index of the current digit
            index = k // factorial
            result.append(numbers.pop(index))
            
            # Update k for the remaining digits
            k %= factorial
            
            # Update factorial for the next position
            n -= 1
            if n > 0:
                factorial //= n
                
        return "".join(result)
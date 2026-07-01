class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1.0
        current_product = x
        
        # Iterative binary exponentiation
        while n > 0:
            # If n is odd, multiply the current product into the result
            if n % 2 == 1:
                result *= current_product
                
            # Square the base and halve the exponent power
            current_product *= current_product
            n //= 2
            
        return result
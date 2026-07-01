class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        seen = set()
        
        def backtrack(current_permutation):
            # Base Case: If the current path matches the length of nums, it's a valid permutation
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            for num in nums:
                # If the number is already used in the current path, skip it
                if num in seen:
                    continue
                
                # Make choices
                current_permutation.append(num)
                seen.add(num)
                
                # Recursively explore the next positions
                backtrack(current_permutation)
                
                # Undo choices (Backtrack)
                current_permutation.pop()
                seen.remove(num)
                
        backtrack([])
        return result
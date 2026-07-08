class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # Step 1: Sort the array to place duplicates adjacent to each other
        nums.sort()
        
        def backtrack(start, current_subset):
            # Add a copy of the current subset to our final list
            result.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # Step 3: Skip duplicate elements at the same recursive level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include the current element
                current_subset.append(nums[i])
                # Move to the next element
                backtrack(i + 1, current_subset)
                # Backtrack: remove the element before moving to the next choice
                current_subset.pop()
                
        backtrack(0, [])
        return result
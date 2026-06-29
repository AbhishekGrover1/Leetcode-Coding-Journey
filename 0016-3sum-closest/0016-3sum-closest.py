class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Sort the array first
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            # Optimization: Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match to the target, return it immediately
                if current_sum == target:
                    return current_sum
                    
                # Update closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                # Move pointers based on how current_sum compares to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
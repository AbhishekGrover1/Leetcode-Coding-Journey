class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
                
            # Critical Duplicate Handling: 
            # If the boundaries and mid are identical, we cannot determine which half is sorted.
            # We safely shrink the search space by shifting both pointers inward.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
                
            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
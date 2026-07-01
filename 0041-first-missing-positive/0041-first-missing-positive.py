class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(n):
            # Place nums[i] in its correct index position (nums[i] - 1) if valid
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap elements to place nums[i] at its target bucket
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Find the first index where the expected number is missing
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all numbers from 1 to n are present, the answer is n + 1
        return n + 1
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_boundary():
            left, right = 0, len(nums) - 1
            boundary = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    boundary = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return boundary
        
        def find_right_boundary():
            left, right = 0, len(nums) - 1
            boundary = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    boundary = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return boundary
        
        if not nums:
            return [-1, -1]
        
        left_pos = find_left_boundary()
        
        if left_pos == -1:
            return [-1, -1]
        
        right_pos = find_right_boundary()
        
        return [left_pos, right_pos]
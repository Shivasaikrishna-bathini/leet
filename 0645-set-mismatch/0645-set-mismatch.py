class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = sum(nums)
        actual_sq_sum = sum(num ** 2 for num in nums)
        
        diff_sum = expected_sum - actual_sum
        diff_sq_sum = expected_sq_sum - actual_sq_sum
        
        duplicate = (diff_sq_sum // diff_sum - diff_sum) // 2
        missing = duplicate + diff_sum
        
        return [duplicate, missing]
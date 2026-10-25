class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        memo = [0] * (n+1)
        memo[n-1] = nums[n-1]
        for j in range(n-2, -1, -1):
            memo[j] = max(nums[j]+memo[j+2], memo[j+1])
        
        return memo[0]
        
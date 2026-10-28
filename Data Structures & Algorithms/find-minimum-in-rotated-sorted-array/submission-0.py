class Solution:
    def findMin(self, nums: List[int]) -> int:
        # thought: find the min, then conduct binary search with that: O(n + logn) = O(n)
        # note: this is like a "cliff", where rises, sudden fall, then rises again. not finding a valley point. 
        # take [3,4,5,6,1,2]: two halves are [3,4,5] and [6,1,2] since 5 < 6, pick higher side (drop is after higher) 
        # repeat until we find drop. if drop at the last index, this 1st element is the min. 
        n = len(nums)
        # left = int(n / 2)
        # right = int((n / 2) + 1) if n >= 2 else 0
        if n == 1:
            return nums[0]
        
        if n == 2 and nums[0] > nums[1]: 
            return nums[1]
        
        right = nums[int(n/2):]
        left = nums[:int(n/2)]
        return min(self.findMin(right), self.findMin(left))
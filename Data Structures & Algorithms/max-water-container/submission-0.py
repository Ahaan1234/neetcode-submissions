class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # naive approach: check all nC2 combinations of bars and pick max area (O(n^2)). 
        # this is the score to beat. check "2 pointers"
        n = len(heights)
        i = 0
        j = n-1
        vol = 0
        while i < j:
            vol = max(vol, min(heights[i], heights[j]) * (j-i))
            if heights[i] < heights[j]: i += 1
            else: j -= 1
        
        return vol

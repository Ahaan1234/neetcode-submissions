class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for _ in range(len(nums) + 1)]
        ret = []
        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1

        for key in counts:
            freqs[counts[key]].append(key)
        
        for i in range(len(freqs)-1, 0, -1):
            ret.extend(freqs[i])

        return ret[:k]
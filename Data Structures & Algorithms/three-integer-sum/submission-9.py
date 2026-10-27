class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        out = set()

        for a in range(0,n):
            if sorted_nums[a] > 0:
                break
            
            if (a > 0 and sorted_nums[a] == sorted_nums[a-1]):
                continue
            j = a + 1
            k = n - 1


            while j < k:
                total = sorted_nums[a] + sorted_nums[j] + sorted_nums[k]
                if total < 0:   
                    j += 1
                elif total > 0: 
                    k -= 1
                else:      
                    out.add((sorted_nums[a],sorted_nums[j],sorted_nums[k]))
                    k -= 1
                    j += 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k + 1]:
                        k -= 1

        
        return list(out)
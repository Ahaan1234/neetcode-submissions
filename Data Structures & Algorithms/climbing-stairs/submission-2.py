class Solution:
    def climbStairs(self, n: int) -> int:
        # subproblem: climbStairs(m) is the number of ways to climb stairs up to step m. domain: 1 ≤ m ≤ n. base case: m ≥ n -> return 0. 
        # from m, can either climb up one stair or two stairs. so climbStairs(m)=climbStairs(m+1)+climbStairs(m+2)
        # evaluation order: m from n to 1 (decreasing)
        # memoize in 1D array of length n.
        if n == 1: return 1
        arr = [0] * n
        # print(arr[n-1])
        arr[n-1] = 1
        arr[n-2] = 2
        for i in range(n-3, -1, -1):
            arr[i] = arr[i+1] + arr[i+2]
        
        return arr[0]
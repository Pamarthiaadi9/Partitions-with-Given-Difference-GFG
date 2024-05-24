from typing import List


class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        mod = 10**9 + 7
        
        total = sum(arr)
        
        if total < d or (total - d) % 2 == 1:
            return 0
        
        target = (total - d) // 2
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
                dp[j] %= mod
        
        return dp[target]

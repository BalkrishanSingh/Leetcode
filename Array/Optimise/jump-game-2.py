from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1 for x in range(len(nums))]
        dp[0] = 0
        for i, num in enumerate(nums):
            if dp[i] != -1:
                j = 0
                while j < num and i + j + 1 < len(nums) :
                    if dp[i+j+1] == -1:
                        dp[i+j+1] = 1 + dp[i]
                    else:
                        dp[i+j+1] = min(dp[i+j+1],dp[i+j+1] + 1)
                    j +=1
        return dp[len(nums) -1] 
            

if __name__ == "__main__":
    solver = Solution()
    result = solver.jump([1,2,3])
    print(f"Input: [1,2,3] | Expected: 2 | Actual: {result} | {'PASS' if result == 2 else 'FAIL'}")
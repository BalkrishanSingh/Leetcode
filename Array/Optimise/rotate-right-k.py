class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        num = nums[::-1]
        num[:k:] = num[k-1::-1]
        num[k::] = num[:k-1:-1]
        for i in range(len(num)):
            nums[i] = num[i]

#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
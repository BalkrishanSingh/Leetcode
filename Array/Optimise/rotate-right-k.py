class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            last_elem = nums[len(nums)-1]
            del nums[len(nums)-1]
            nums.insert(0, last_elem)

#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
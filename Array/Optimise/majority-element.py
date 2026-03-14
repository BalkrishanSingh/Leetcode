class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash:dict[int,int] = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] +=1
            else: 
                hash[nums[i]] = 1
            if hash[nums[i]] >= len(nums)/2:
                return nums[i]
#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
       
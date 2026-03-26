from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left:int = 0
        right:int = len(numbers) -1

        while left < right:
            if target - numbers[right] == numbers[left]:
                return [left+1,right+1]
            if target - numbers[right] > numbers[left]:
                left +=1
            else:
                right -=1
        return [-1,-1] # if there is no two sum
            
S = Solution()
print(S.twoSum( numbers = [2,3,4], target = 6))
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
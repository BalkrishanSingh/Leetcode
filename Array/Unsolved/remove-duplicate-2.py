from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i:int = 0 # replacable number
        k:int = 1# forward mover
        num:int = nums[i] #current number
        c:int = 1 #count
        while k < len(nums):
            if num == nums[k] and c < 2:
                nums[i+1] = nums[k]
                i+=1
                k+=1
                c+=1
            elif num == nums[k] and c >= 2:
                k+=1
            else:
                nums[i+1] = nums[k]
                num = nums[i+1]
                c = 1
                i+=1

        return i
#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
        
if __name__ == "__main__":
    solution = Solution()
    
    def run_test(test_name, nums, expected_k, expected_nums):
        original_nums = nums.copy()
        
        # Edge case for empty array that might break the user's logic
        # if the user hasn't handled it yet.
        try:
            k = solution.removeDuplicates(nums)
        except Exception as e:
            print(f" {test_name} failed with Exception: {e}")
            print(f"   Original nums: {original_nums}")
            return
            
        try:
            assert k == expected_k, f"Expected length {expected_k}, got {k}"
            # The problem states the first k elements of nums should contain the result
            actual_nums = nums[:k]
            assert actual_nums == expected_nums, f"Expected elements {expected_nums}, got {actual_nums}"
            print(f"{test_name} passed!")
        except AssertionError as e:
            print(f" {test_name} failed: {e}")
            print(f"   Original nums: {original_nums}")

    # Provided test case
    run_test("Test Case 1", [0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3])
    
    # Standard test case
    # run_test("Test Case 2", [1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3])
    
    # Other potential cases for problem 80
    # run_test("Empty Array", [], 0, [])
    # run_test("All Elements Match", [2, 2, 2, 2], 2, [2, 2])
    # run_test("No Elements Match", [1, 2, 3], 3, [1, 2, 3])
    # run_test("Single Element", [1], 1, [1])
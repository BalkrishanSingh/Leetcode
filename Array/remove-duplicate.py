from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i:int = 0 # last confirmed unique
        k:int = 1# forward mover
        while k < len(nums):
            if nums[i] == nums[k]:
                k+=1
                
            else:
                nums[i+1] = nums[k]
                i+=1
                k+=1
        return i+1
                



if __name__ == "__main__":
    solution = Solution()
    
    def run_test(test_name, nums, expected_k, expected_nums):
        original_nums = nums.copy()
        k = solution.removeDuplicates(nums)
        
        try:
            assert k == expected_k, f"Expected length {expected_k}, got {k}"
            actual_nums = nums[:k]
            assert actual_nums == expected_nums, f"Expected elements {expected_nums}, got {actual_nums}"
            print(f"{test_name} passed!")
        except AssertionError as e:
            print(f" {test_name} failed: {e}")
            print(f"   Original nums: {original_nums}")
            
    # Standard cases
    # run_test("Test Case 1", [1, 1, 2], 2, [1, 2])
    run_test("Test Case 2", [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    
    # Edge cases
    # run_test("Empty Array", [], 0, [])
    # run_test("All Elements Match", [2, 2, 2], 1, [2])
    # run_test("No Elements Match", [1, 2, 3], 3, [1, 2, 3])
    # run_test("Single Element", [1], 1, [1])

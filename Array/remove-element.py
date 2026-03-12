from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hash: dict[str, int] = {"match":0}
        i:int=len(nums) - 1
        j:int=len(nums) - 1
        temp: int
        while i >= 0:
            if nums[i] == val:
                temp = nums[j]
                nums[j] == val
                nums[i] = nums[j]
                hash["match"] +=1
                j -=1
            i -=1
        return len(nums) -  hash["match"]
        
        

if __name__ == "__main__":
    solution = Solution()
    
    def run_test(test_name, nums, val, expected_k, expected_nums):
        original_nums = nums.copy()
        k = solution.removeElement(nums, val)
        
        try:
            assert k == expected_k, f"Expected length {expected_k}, got {k}"
            # The problem states the order of elements may be changed. 
            # It doesn't matter what you leave beyond the returned k.
            actual_nums = sorted(nums[:k])
            expected_nums_sorted = sorted(expected_nums)
            assert actual_nums == expected_nums_sorted, f"Expected elements {expected_nums_sorted}, got {actual_nums}"
            print(f"{test_name} passed!")
        except AssertionError as e:
            print(f" {test_name} failed: {e}")
            print(f"   Original nums: {original_nums}, val: {val}")
    
    # Standard cases
    run_test("Test Case 1", [3, 2, 2, 3], 3, 2, [2, 2])
    run_test("Test Case 2", [0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4])
    
    # Edge cases
    run_test("Empty Array", [], 0, 0, [])
    run_test("All Elements Match", [2, 2, 2], 2, 0, [])
    run_test("No Elements Match", [1, 2, 3], 4, 3, [1, 2, 3])
    run_test("Single Element - Match", [1], 1, 0, [])
    run_test("Single Element - No Match", [1], 2, 1, [1])
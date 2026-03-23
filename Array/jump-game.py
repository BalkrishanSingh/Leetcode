class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest_point = 0
        for i, distance in enumerate(nums):
            if farthest_point >= len(nums) -1:
                return True
            if i <= farthest_point:
                if farthest_point < i+distance:
                    farthest_point = distance +i
            else:
                return False
        return True


def run_basic_tests() -> None:
    solver = Solution()
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]

    for nums, expected in test_cases:
        actual = solver.canJump(nums)
        status = "PASS" if actual == expected else "FAIL"
        print(f"{status} | nums={nums} | expected={expected} | actual={actual}")


if __name__ == "__main__":
    run_basic_tests()


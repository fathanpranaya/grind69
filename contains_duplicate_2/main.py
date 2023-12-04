class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {key:[] for key in nums}


if __name__ == "__main__":
    # Test your solution
    nums = [1, 2, 3, 1]
    solution = Solution()
    print(solution.contains_duplicate(nums))  # Expected output: True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in num_map:
                return True
            num_map[nums[i]] = num_map.get(nums[i], 0) + 1

        return False
        
    
if __name__ == "__main__":
    solution = Solution()
    # nums = [1,1,1,3,3,4,3,2,4,2]
    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums))

class Solution:
    def twoSumBruteForce(self, nums: [int], target: int) -> [int]:
        n = len(nums)
        # Your implementation of the twoSum method goes here
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []
    
    def twoSumHashMap(self, nums:[int], target:int) -> [int]:
        num_map = {}
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]
            if complement in num_map:
                return [i, num_map[complement]]
            num_map[nums[i]] = i
            print(num_map)
        
        return []


if __name__ == "__main__":
    # Your main program logic goes here
    
    nums = [2,7,11,15]
    target = 56
    
    # nums = [3,2,4]
    # target = 6


    solution = Solution()
    print(solution.twoSumHashMap(nums, target))
    

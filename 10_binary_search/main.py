from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 #first index of nums
        right = len(nums)# last index of nums

        while left <= right: # iterate until left pointer is > right
            # tracking/simulate the binary search
            print(nums[left:right])

            # calculate mid pointer -> median
            mid = (left + right) // 2
            # check if the target match return mid (index)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]: # target is within lower bracket -> shift right pointer to mid - 1
                right = mid - 1
            else: # target is within upper bracket -> shift left pointer to mid + 1
                left = mid + 1

            
        
        # if not found (out from loop)
        return -1

# test case
if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 12
    print(sol.search(nums, target))
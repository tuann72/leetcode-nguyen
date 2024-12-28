from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TODO: create a left and right variable to store boundary
        left, right = 0, len(nums) - 1

        # TODO: loop till left = right
        while left <= right:
            # TODO: create middle point
            middle = (left + right) // 2

            # TODO: check if middle is target
            if nums[middle] == target:
                return middle

            # TODO: check if target is less than middle
            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1


sol = Solution()
test = sol.search([-1, 0, 3, 5, 9, 12], 2)
print(test)

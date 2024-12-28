from typing import List
from math import floor


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        given: list of numbers, and a target number
        return: if target number is in list return index, otherwise return where it would be inserted into sorted order
        """

        # Find if target number exist using binary search
        # TODO: create left and right index
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            # TODO: find middle index
            middle_index = (left_index + right_index) // 2

            # TODO: check if middle index is target
            if nums[middle_index] == target:
                return middle_index

            # TODO: if target is less than middle, look to left side
            if target < nums[middle_index]:
                # right_index is not just middle index but middle_index - 1 because we don't need to check middle index again
                right_index = middle_index - 1
            else:
                # same logic as the right_index
                left_index = middle_index + 1

        """
        return left because of the following two scenarios below
        given [2], target = 1, then L = R. In this case 1 < 2 so updated variable would be R < L, L = 0 which is where 1 needs to be inserted into
        given [2], target = 3, then L = R. In this case 2 > 3 so updated variable would be R > L, L would be shifted over one index to the right which is where 3 would be inserted into
        """
        return left_index


solution = Solution()
test1 = solution.searchInsert([1, 3, 5, 6], 5)
test2 = solution.searchInsert([1, 3, 5, 6], 2)

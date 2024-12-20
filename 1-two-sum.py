from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        return indices of two numbers such that they add up to target number
        given: list = [1,2,3], target = 5
        process: list[1] + list[2] = 2 + 3 = 5
        return: 1, 2
        """

        """TODO: Loop through list to find left part of addition"""
        # for left_index in range(len(nums)):
        """
        TODO: Loop through list to find right part of addition
        NOTE: total number of values of right num decreases per outer loop finish
        Trick: we know we cannot add the same index, so right_index starts at 1 instead of 0 ...
        additionally we it to decrease over time so we add left_index with 1 to start the ...
        right index always to the "right" of the left index.
        """
        # for right_index in range(left_index + 1, len(nums)):
        #     if nums[left_index] + nums[right_index] == target:
        #         return [left_index, right_index]

        """
        Can this be solved faster than O(n^2)?
        NOTE: simply code to single loop
        TRICK: use hashmap, "in" function in Python has O(1) average time complexity...
        so the total time complexity of the code below is O(n).
        """

        """
        TODO: create hashmap to contain value and index
        NOTE: dict = value : index
        """
        hashmapNums = {}
        """TODO: Loop through list to operate on"""
        for index, number in enumerate(nums):
            """TODO: Find the complement to the target - current number from loop"""
            complement = target - number
            """TODO: Check to see if complement exist"""
            if complement in hashmapNums:
                """
                return hashmapNums[complement] first because this would be the old number, index would belong to new number...
                this is because first iteration will always end up adding a new hash value and index
                """
                return [hashmapNums[complement], index]
            """TODO: Add number and its index to hashmap to be checked during next loop"""
            hashmapNums[number] = index
        return []


if __name__ == "__main__":
    solution = Solution()
    test1 = solution.twoSum([1, 2, 3, 4], 7)
    print(test1)

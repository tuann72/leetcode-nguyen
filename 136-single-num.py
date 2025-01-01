from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        given: list of number
        return: number that is not a pair
        process: use XOR operation, remember XOR operation is communitive, XOR same number results in 0. Think XOR canceling our pairs.
        """
        res = 0
        # TODO: loop through each number
        for number in nums:
            # XOR each number, start with 0 because num XOR 0 = num
            res = number ^ res
        return res


sol = Solution()
test1 = sol.singleNumber([1, 2, 1, 2, 4])
print(test1)

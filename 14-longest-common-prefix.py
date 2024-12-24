from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        given: list of strings
        returns: common prefix
        process: select a first word as comparison, loop through first words characters to see if it exist in every other string
        """
        answer = ""

        # TODO: Create a loop that holds the index for each character we will compare
        for i in range(len(strs[0])):
            # TODO: Loop through the strings in the list
            for string in strs:
                # Check two conditions
                # 1. If the index we are on is larger than the string being compared to than return answer, i.e. flower and flow will stop at flow
                # 2. If the character in index i of the strings in the list does not equal the strings in our first word then return answer
                # i.e. flow and flop do not have some character at index 3.
                if i == len(string) or string[i] != strs[0][i]:
                    return answer
            # If all strings fail the condition, only then can we append the character to answer because we know that
            # all strings must contain the character in the same index
            answer += strs[0][i]
        return answer

solution = Solution()
test1 = solution.longestCommonPrefix(["dog", "dogma", "doodoo"])
test2 = solution.longestCommonPrefix(["flower","flow","flight"])
test3 = solution.longestCommonPrefix(["dog","racecar","car"])
print(test1)
print(test2)
print(test3)

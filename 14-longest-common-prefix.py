from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer

solution = Solution()
test1 = solution.longestCommonPrefix(["dog", "dogma", "doodoo"])
test2 = solution.longestCommonPrefix(["flower","flow","flight"])
test3 = solution.longestCommonPrefix(["dog","racecar","car"])
print(test1)
print(test2)
print(test3)

class Solution:
    def isValid(self, s: str) -> bool:
        return True


solution = Solution()
test1 = solution.isValid("(){}[]")
test2 = solution.isValid("(]")
test3 = solution.isValid("([])")

print(test1)
print(test2)
print(test3)

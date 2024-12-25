class Solution:
    def isValid(self, s: str) -> bool:
        """
        given: string made of [], (), {}
        return: if the parentheses are being used correctly
        process: add each character in the string to a stack, if a character we are evaluting is a pair to the top of the stack then we pop it off
        """

        stack = []

        # NOTE: the hashmap is pairing closed to open not open to closed.
        # The reasoning is that we only remove from stack if a closed is recieved
        dict = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        # TODO: create a loop which goes through each character
        for character in s:
            # TODO: check if character is in the dict (is the character a closed parentheses)
            if character in dict:
                # TODO: check if there are elements in stack (is there open parentheses) and check if the element at the top of the stack corresponds to the character's pair in the hashmap
                if stack and stack[-1] == dict[character]:
                    # TODO: pop the open parentheses when the closed is found
                    stack.pop()
                else:
                    return False
            # TODO: if we notice the character is not in the hashmap (is a open parentheses) then we append it to stack
            else:
                stack.append(character)
        # TODO: return stack if stack is empty otherwise false (case where it could be false is where it has only open parentheses)
        return True if not stack else False


solution = Solution()
test1 = solution.isValid("(){}[]")
test2 = solution.isValid("(]")
test3 = solution.isValid("([])")
print(test1)
print(test2)
print(test3)

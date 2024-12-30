class Solution:
    def climbStairs(self, n: int) -> int:
        """
        given: n steps to reach to top
        return: number of ways to reach to top using combination of steps of 1 or 2
        """
        # memorize patterns that have been solved
        memo = {1: 1, 2: 2}

        # create function to recursively call
        def f(n: int):
            # check if n is in memo
            if n in memo:
                # return the item in the memo (we already solved)
                return memo[n]
            else:
                # add new item to meme
                memo[n] = f(n - 2) + f(n - 1)
                # return item we just added
                return memo[n]

        return f(n)


solution = Solution()
test = solution.climbStairs(10)
print(test)

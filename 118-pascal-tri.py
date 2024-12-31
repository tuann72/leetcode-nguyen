from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        given: a number of rows
        return: return corresponding rows of pascal triangle
        process: sum each adjacent number up
        """

        # set res to contain first 2 rows
        res = [[1], [1, 1]]

        # address base cases where user enters 1 or 2
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        # loop through numRows - 2 times, each time append a new row (we subtract 2 because we manually entered the first 2 rows)
        for i in range(numRows - 2):
            # create a variable to shorthand find the size of res
            sizeOfRes = len(res) - 1
            # store temporary list which contains the next row
            temp = []
            # append 1 to the beginning because pascal's triangle rule
            temp.append(1)
            # loop the through each of res's most recent rows element except the last one, offset so we can add adjacency numbers
            for j in range(len(res[sizeOfRes]) - 1):
                # append the sum of the adjaceny numbers to temp
                temp.append(res[sizeOfRes][j] + res[sizeOfRes][j + 1])
            # append the last 1 in the row
            temp.append(1)
            # append to res
            res.append(temp)

        return res


sol = Solution()
test1 = sol.generate(3)
test2 = sol.generate(5)
print(test1)
print(test2)

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        given: roman numeral
        returns integer value of roman numeral
        process: split roman numerals up, find its integer counterpart
        """

        # NOTE: IV = 4, VI = 6, if the left roman numeral is smaller than right, subtract right from left otherwise add
        total = 0
        mapping = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        # TODO: Convert roman numeral string into seperate characters.
        romanNumChar = list(s)
        romanInt = []
        # TODO: Convert characters into integer values
        for index, character in enumerate(romanNumChar):
            if character in mapping:
                romanInt.append(mapping[character])
        # TODO: Perform math operation based on their values
        # total will keep track of current numerals added
        total += 0
        # prev_num will be part of the comparison for the pair
        prev_num = 0
        """
        TRICK: start backwards, roman numerals work in pairs, starting backwards allows you to pair correctly
        i.e. MCMXCIV, if you start in the beginning you would check if MC is a pair but that is incorrect since it
        needs to broken does as M, CM, XC, IV. in this case we noticed that M is not paired.

        Alternate idea could be that you start with C and check the right numeral M. At the end you can add M from the start.
        """
        # idx value starts at the end of romanInt and moves to 0
        for idx in range(len(romanInt)-1, -1, -1):
            # i.e. VI = V > I, then add 5 + 1
            if(prev_num <= romanInt[idx]):
                total += romanInt[idx]
            # else IV results in 5 - 1
            else:
                total -= romanInt[idx]
            # update prev_num to next number
            prev_num = romanInt[idx]

        return total

if __name__ == "__main__":
    solution = Solution()
    t1 = solution.romanToInt("IV")
    t2 = solution.romanToInt("VII")
    t3 = solution.romanToInt("MCMXCIV")
    print(t1)
    print(t2)
    print(t3)

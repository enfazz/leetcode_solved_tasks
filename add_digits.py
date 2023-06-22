# https://leetcode.com/problems/add-digits/description/

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0


# Constraints:

# 0 <= num <= 231 - 1

# Simple iteration through all digits of the num variable intil single digit number is created 
class Solution:
    def addDigits(self, num: int) -> int:
        counter = num
        while counter >= 10:
            digits = [int(x) for x in str(counter)]
            counter = 0
            for i in digits:
                counter += i
        return counter

# Follow up: Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: 
            return 0
        return num % 9 or 9
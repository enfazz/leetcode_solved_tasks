# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 

# Constraints:

# -231 <= n <= 231 - 1

# I will iterate through specified primes and divide n by each prime in desc order and check,
# if after all divisions it will == 1
class Solution:
    def isUgly(self, n: int) -> bool:
        valid_primes = [5, 3, 2]
        if n <= 0:
            return False
        for prime in valid_primes:
            while n % prime == 0:
                n /= prime
        return n == 1
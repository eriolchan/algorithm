"""Reverse Integer.

Given a 32-bit signed integer, reverse digits of an integer.

https://leetcode.com/problems/reverse-integer/

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed integer
overflows.
"""


import unittest


class Solution(object):

    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        threshold = MAX // 10
        remainder = MAX % 10 + 1 if x < 0 else MAX % 10
        sign = -1 if x < 0 else 1
        x *= sign
        reversed = 0
        while x:
            if reversed > threshold or (reversed == threshold and x > remainder):
                return 0
            reversed = reversed * 10 + x % 10
            x = x // 10
        return reversed * sign


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_positive(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_negative(self):
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_end_with_zero(self):
        self.assertEqual(self.solution.reverse(120), 21)

    def test_zero(self):
        self.assertEqual(self.solution.reverse(0), 0)

    def test_even_digit(self):
        self.assertEqual(self.solution.reverse(23), 32)

    def test_one_digit(self):
        self.assertEqual(self.solution.reverse(3), 3)

    def test_positive_overflow(self):
        self.assertEqual(self.solution.reverse(2147483647), 0)

    def test_negative_overflow(self):
        self.assertEqual(self.solution.reverse(-2147483647), 0)

    def test_invalid_input(self):
        self.assertEqual(self.solution.reverse(2 ** 31), 0)


if __name__ == '__main__':
    unittest.main()

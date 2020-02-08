import unittest


"""
Reverse Integer.
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

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


class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        threshold = MAX // 10
        remainder = MAX % 10 + 1 if x < 0 else MAX % 10
        sign = -1 if x < 0 else 1
        x *= sign
        reversed = 0
        while x:
            if reversed == threshold and x > remainder or reversed > threshold:
                return 0
            reversed = reversed * 10 + x % 10
            x = x // 10
        return sign * reversed


class TestSolution(unittest.TestCase):
    def test_positive(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)

    def test_negative(self):
        s = Solution()
        self.assertEqual(s.reverse(-123), -321)

    def test_end_with_zero(self):
        s = Solution()
        self.assertEqual(s.reverse(120), 21)

    def test_zero(self):
        s = Solution()
        self.assertEqual(s.reverse(0), 0)

    def test_positive_overflow(self):
        s = Solution()
        self.assertEqual(s.reverse(2147483647), 0)

    def test_negative_overflow(self):
        s = Solution()
        self.assertEqual(s.reverse(-2147483647), 0)

    def test_invalid_input(self):
        s = Solution()
        self.assertEqual(s.reverse(2 ** 31), 0)


if __name__ == '__main__':
    unittest.main()

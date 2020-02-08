import unittest


"""
Palindrome Number.
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes
121-. Therefore it is not a palindrome.

Example 3:
    Input: 10
    Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""


class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x):
            return False
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x = x // 10
        return x == reversed or x == reversed // 10


class TestSolution(unittest.TestCase):
    def test_positive(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(121), True)

    def test_negative(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(-121), False)

    def test_end_with_zero(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(10), False)

    def test_palindrome_with_zero(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(200200), False)

    def test_not_palindrome(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(123), False)

    def test_same(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(111), True)

    def test_even_digit(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(2002), True)

    def test_one_digit(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(3), True)

    def test_zero(self):
        s = Solution()
        self.assertEqual(s.is_palindrome(0), True)


if __name__ == '__main__':
    unittest.main()

from typing import List
import unittest


"""
Two Sum.
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if (complement in seen):
                return [seen[complement], i]
            seen[num] = i
        raise RuntimeError('No solution')


class TestSolution(unittest.TestCase):
    def test_different_value(self):
        s = Solution()
        self.assertEqual(s.two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_same_value(self):
        s = Solution()
        self.assertEqual(s.two_sum([3, 3, 4], 6), [0, 1])

    def test_not_use_twice(self):
        s = Solution()
        self.assertEqual(s.two_sum([3, 2, 4], 6), [1, 2])

    def test_no_solution(self):
        s = Solution()
        with self.assertRaises(RuntimeError):
            s.two_sum([1, 2, 3], 6)

    def test_one_element(self):
        s = Solution()
        with self.assertRaises(RuntimeError):
            s.two_sum([1], 1)


if __name__ == '__main__':
    unittest.main()

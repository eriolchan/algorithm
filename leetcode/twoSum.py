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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidate = {}
        for i, num in enumerate(nums):
            if (num in candidate):
                return [candidate[num], i]
            candidate[target - num] = i
        raise RuntimeError('No two sum solution')


class TestSolution(unittest.TestCase):
    def test_different_value(self):
        s = Solution()
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])

    def test_same_value(self):
        s = Solution()
        self.assertEqual(s.twoSum([3, 3, 4], 6), [0, 1])

    def test_no_solution(self):
        s = Solution()
        with self.assertRaises(RuntimeError):
            s.twoSum([1, 2, 3], 6)

    def test_one_element(self):
        s = Solution()
        with self.assertRaises(RuntimeError):
            s.twoSum([1], 1)


if __name__ == '__main__':
    unittest.main()

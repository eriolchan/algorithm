"""Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

https://leetcode.com/problems/implement-strstr/

Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question
to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().
"""


from typing import List
import unittest


class Solution(object):

    def str_str(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if not needle_len:
            return 0
        # Boyer-Moore algorithm
        bad_character = self.get_bad_character(needle)
        good_suffix = self.get_good_suffix(needle)
        start = 0
        end = haystack_len - needle_len
        while start <= end:
            for i in range(needle_len - 1, -1, -1):
                if haystack[start+i] != needle[i]:
                    start += max(bad_character[ord(haystack[start+i])] - (needle_len - 1 - i),
                                 good_suffix[i])
                    break
            else:
                return start
        return -1

    def get_bad_character(self, pattern: str) -> List[int]:
        pattern_len = len(pattern)
        bad_character = [pattern_len] * 256
        last_index = pattern_len - 1
        for i in range(last_index):
            bad_character[ord(pattern[i])] = last_index - i
        return bad_character

    def get_good_suffix(self, pattern: str) -> List[int]:
        suffix = self.get_suffix(pattern)
        pattern_len = len(pattern)
        good_suffix = [pattern_len] * pattern_len
        last_index = pattern_len - 1
        for i in range(last_index, -1, -1):
            if suffix[i] == i + 1:
                for j in range(last_index - i):
                    if good_suffix[j] == pattern_len:
                        good_suffix[j] = last_index - i
        for i in range(last_index):
            good_suffix[last_index-suffix[i]] = last_index - i
        return good_suffix

    def get_suffix(self, pattern: str) -> List[int]:
        pattern_len = len(pattern)
        suffix = [0] * pattern_len
        last_index = pattern_len - 1
        suffix[last_index] = pattern_len
        last_end = last_index
        for i in range(last_index - 1, -1, -1):
            if i > last_end and suffix[last_index-(last_start-i)] < i - last_end:
                suffix[i] = suffix[last_index-(last_start-i)]
            else:
                if i < last_end:
                    last_end = i
                last_start = i
                while last_end >= 0 and pattern[last_end] == pattern[last_index-(last_start-last_end)]:
                    last_end -= 1
                suffix[i] = last_start - last_end
        return suffix


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_find(self):
        self.assertEqual(self.solution.str_str('hello', 'll'), 2)

    def test_not_find(self):
        self.assertEqual(self.solution.str_str('aaaaaa', 'bba'), -1)

    def test_first_occurence(self):
        self.assertEqual(self.solution.str_str('ababcabc', 'abc'), 2)

    def test_haystack_short_than_needle(self):
        self.assertEqual(self.solution.str_str('ab', 'abc'), -1)

    def test_empty_haystack(self):
        self.assertEqual(self.solution.str_str('', 'abc'), -1)

    def test_empty_needle(self):
        self.assertEqual(self.solution.str_str('', ''), 0)


if __name__ == '__main__':
    unittest.main()

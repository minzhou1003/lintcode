"""
200. Longest Palindromic Substring
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".

Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
"""
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    # O(n^2)
    def longestPalindrome(self, s):
        # write your code here
        res_left, res_right, max_length = 0, 1, 0
        n = len(s)
        for i in range(1, n * 2):
            if i & 1: # odd
                left = i // 2
                right = left
            else: # even
                left = i // 2 - 1
                right = left + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > max_length:
                max_length = right - left
                res_left = left
                res_right = right
        return s[res_left:res_right + 1]
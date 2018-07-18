"""
627. Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        dic = set()
        for char in s:
            if char in dic:
                dic.discard(char)
            else:
                dic.add(char)
        remove = len(dic)
        if remove > 0:
            remove -= 1
        return len(s) - remove
"""
143. Sort Colors II
Given an array of n objects with k different colors (numbered from 1 to k), 
sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. 
That will cost O(k) extra memory. Can you do it without using extra memory?
"""
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or len(colors) == 0:
            return colors

        self.sort_color(colors, 0, len(colors)-1, 1, k)
    
    def sort_color(self, colors, left, right, color_from, color_to):
        if color_from == color_to:
            return
        if left >= right:
            return
        
        mid_color = (color_from + color_to) // 2
        l = left
        r = right
        while(l <= r):
            while(l <= r) and colors[l] <= mid_color:
                l += 1
            while(l <= r) and colors[r] > mid_color:
                r -= 1
            if l < r:
                colors[l], colors[r] = colors[r], colors[l]
                l += 1
                r -= 1
        self.sort_color(colors, left, r, color_from, mid_color)
        self.sort_color(colors, l, right, mid_color + 1, color_to)
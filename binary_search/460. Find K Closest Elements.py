"""
460. Find K Closest Elements
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.
"""
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        # find the closest number
        start = 0
        end = len(A) - 1
        while start + 1< end:
            mid = start + (end-start) //2
            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        res = []
        # add k numbers
        while len(res) != k:
            diff_left = abs(A[start] - target) if start >= 0 else None
            diff_right = abs(A[end] - target) if end < len(A) else None
            if diff_left !=None and diff_right != None:
                if diff_left <= diff_right: # if equal add left
                    res.append(A[start])
                    start -= 1
                else:
                    res.append(A[end])
                    end += 1
            elif diff_left == None:
                res.append(A[end])
                end += 1
            elif diff_right == None:
                res.append(A[start])
                start -= 1
        return res

# O(logn) Method
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        res = []
        for i in range(k):
            closest = self.FindClosestNumber(A, target)
            res.append(A[closest])
            A.pop(closest) # pop index
        return res

    def FindClosestNumber(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if abs(A[start] - target) <= abs(A[end] - target):
            return start
        else:
            return end
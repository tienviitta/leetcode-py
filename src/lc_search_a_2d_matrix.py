from typing import List
import numpy as np


class Solution:
    def searchMatrixOrig(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = np.array(matrix).ravel()
        left, right = int(0), int(mat.size - 1)
        while left <= right:
            mid = (left + right) // 2
            if mat[mid] == target:
                return True
            if mat[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


def test_ex1():
    """
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true
    """
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    ref = True
    res = sol.searchMatrix(matrix, target)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
    """
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    ref = False
    res = sol.searchMatrix(matrix, target)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()

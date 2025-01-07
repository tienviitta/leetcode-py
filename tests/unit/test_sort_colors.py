from src.lc_sort_colors import Solution


def test_sort_colors():
    """
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    """
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_sort_colors_sort():
    """
    Input: nums  = [2,0,1]
    Output: [0,1,2]
    """
    sol = Solution()
    nums = [2, 0, 1]
    sol.sortColors(nums)
    assert nums == [0, 1, 2]

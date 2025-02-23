"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1, 3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1, 2, 3] and median is 2.
Example 2:
    Input: nums1 = [1, 2], nums2 = [3, 4]
    Output: 2.50000
    Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()

    nums_len: int = len(nums1)
    mid: int = (nums_len - 1) // 2

    if nums_len % 2 == 0:
        return (nums1[mid] + nums1[mid + 1]) / 2
    else:
        return nums1[mid]


if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == 5.5
    assert find_median_sorted_arrays([1, 3, 5, 7, 9], [2, 4, 6, 8]) == 5

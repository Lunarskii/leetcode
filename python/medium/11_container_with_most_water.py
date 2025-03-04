"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7].
        In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
    Input: height = [1, 1]
    Output: 1
"""


def max_area(height: list[int]) -> int:
    left: int = 0
    right: int = len(height) - 1
    tallest_wall: int = max(height)
    result: int = 0

    while left < right:
        distance: int = right - left
        if (left_height := height[left]) < height[right]:
            area: int = left_height * distance
            left += 1
        else:
            area: int = height[right] * distance
            right -= 1
        if tallest_wall * distance < result:
            break
        if result < area:
            result = area
    return result


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([1, 8, 8, 1]) == 8
    assert max_area([1, 8, 8, 6, 1]) == 12
    assert max_area([1, 8, 8, 5, 1]) == 10
    assert max_area([1, 8, 8, 4, 3, 1]) == 9
    assert max_area([1000, 8, 8, 4, 3, 1]) == 16

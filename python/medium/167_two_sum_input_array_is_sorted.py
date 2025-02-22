"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:
    Input: numbers = [2, 3, 4], target = 6
    Output: [1, 3]
    Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].
Example 3:
    Input: numbers = [-1, 0], target = -1
    Output: [1, 2]
    Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    left: int = 0
    right: int = len(numbers) - 1

    while left < right:
        two_numbers_sum: int = numbers[left] + numbers[right]

        if two_numbers_sum == target:
            return [left + 1, right + 1]
        elif two_numbers_sum > target:
            right -= 1
        else:
            left += 1


# For very large data
# def two_sum(numbers: list[int], target: int) -> list[int]:
    # left: int = 0
    # right: int = len(numbers) - 1
    #
    # while right > 0:
    #     mid: int = (right + 1) // 2
    #     if numbers[0] + numbers[mid] > target:
    #         right = mid - 1
    #     elif numbers[0] + numbers[mid] == target:
    #         return [1, mid + 1]
    #     else:
    #         break
    #
    # while left < right:
    #     two_numbers_sum: int = numbers[left] + numbers[right]
    #
    #     if two_numbers_sum == target:
    #         return [left + 1, right + 1]
    #     elif two_numbers_sum > target:
    #         right -= 1
    #     else:
    #         left += 1
    #
    # return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    assert two_sum([3, 24, 50, 79, 88, 150, 345], 200) == [3, 6]

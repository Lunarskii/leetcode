"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


# without converting the integer to a string
def is_palindrome(x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    reversed_half: int = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10


# with converting
# def is_palindrome(x: int) -> bool:
#     if x < 0 or (x != 0 and x % 10 == 0):
#         return False
#     return str(x) == str(x)[::-1]


if __name__ == "__main__":
    assert is_palindrome(121)
    assert not is_palindrome(-121)
    assert not is_palindrome(10)
    assert is_palindrome(1221)
    assert is_palindrome(12321)
    assert not is_palindrome(12345)

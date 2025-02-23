"""
Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


def longest_palindrome(s: str) -> str:
    s_len = len(s) - 1
    left: int = 0
    right: int = 0
    palindrome_left: int = 0
    palindrome_right: int = 0

    while right < s_len:
        while right < s_len and s[right + 1] == s[right]:
            right += 1

        temp_right: int = right
        while left > 0 and temp_right < s_len and s[left - 1] == s[temp_right + 1]:
            left -= 1
            temp_right += 1

        if temp_right - left > palindrome_right - palindrome_left:
            palindrome_left = left
            palindrome_right = temp_right

        left = right = right + 1
    return s[palindrome_left:palindrome_right + 1]


if __name__ == "__main__":
    assert longest_palindrome("cbbdbb") == "bbdbb"
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("abbca") == "bb"
    assert longest_palindrome("abbba") == "abbba"
    assert longest_palindrome("abba") == "abba"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("aaaa") == "aaaa"

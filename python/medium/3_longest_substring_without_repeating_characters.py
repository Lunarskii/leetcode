"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(text: str) -> int:
    substring: str = ""
    max_substring_len: int = 0

    for char in text:
        if char in substring:
            substring_len = len(substring)
            if max_substring_len < substring_len:
                max_substring_len = substring_len
            substring = substring.split(sep=char, maxsplit=1)[-1]
        substring += char
    return max(max_substring_len, len(substring))


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("abcdef") == 6
    assert length_of_longest_substring(" ") == 1

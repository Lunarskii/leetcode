"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows.

Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
Example 3:
    Input: s = "A", numRows = 1
    Output: "A"
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    result: list[str] = [""] * num_rows
    line: int = 0
    step: int = -1

    num_rows -= 1
    for char in s:
        result[line] += char
        if line == num_rows or line == 0:
            step = -step
        line += step
    return "".join(result)


if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"
    assert convert("ABCDEF", 1_000_000) == "ABCDEF"
    assert convert("ABCDEF", 3) == "AEBDFC"
    assert convert("", 3) == ""
    assert convert("ABCDEF", 1) == "ABCDEF"

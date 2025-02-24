"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
    1. Whitespace: Ignore any leading whitespace (" ").
    2. Signedness: Determine the sign by checking if the next character is '-' or '+',
    assuming positivity if neither present.
    3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end
    of the string is reached. If no digits were read, then the result is 0.
    4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the
    integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers
    greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
    Input: s = "42"
    Output: 42
    Explanation:
    The underlined characters are what is read in and the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
             ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "42" ("42" is read in)
               ^

Example 2:
    Input: s = " -042"
    Output: -42
    Explanation:
    Step 1: "   -042" (leading whitespace is read and ignored)
                ^
    Step 2: "   -042" ('-' is read, so the result should be negative)
                 ^
    Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
                   ^

Example 3:
    Input: s = "1337c0d3"
    Output: 1337
    Explanation:
    Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
             ^
    Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
                 ^

Example 4:
    Input: s = "0-1"
    Output: 0
    Explanation:
    Step 1: "0-1" (no characters read because there is no leading whitespace)
             ^
    Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
              ^

Example 5:
    Input: s = "words and 987"
    Output: 0
    Explanation:
    Reading stops at the first non-digit character 'w'.
"""
import string


def my_atoi(s: str) -> int:
    s = s.lstrip()
    len_s: int = len(s)
    idx: int = 0

    if len_s == 0:
        return 0
    
    if s[0] in ("+", "-"):
        idx += 1
    while idx < len_s:
        if s[idx] not in string.digits:
            break
        idx += 1
    s = s[0:idx]
    len_s = len(s)
    if len_s >= 1 and not (len_s == 1 and s[0] in ("+", "-")):
        result: int = int(s)
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        return result
    return 0


if __name__ == "__main__":
    assert my_atoi("42") == 42
    assert my_atoi("   -042") == -42
    assert my_atoi("1337c0d3") == 1337
    assert my_atoi("0-1") == 0
    assert my_atoi("words and 987") == 0
    assert my_atoi("") == 0
    assert my_atoi("a") == 0
    assert my_atoi("-2147483649") == -2147483648
    assert my_atoi("2147483648") == 2147483647
    assert my_atoi("+-12") == 0

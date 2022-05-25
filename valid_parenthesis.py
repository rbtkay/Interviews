# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'.
# Determine if the input string is valid.

# An input string is valid if:

# -   Open brackets must be closed by the same type of brackets.
# -   Open brackets must be closed in the correct order.

def is_valid(s: str):
    stack = []
    char_match = {'(': ')', '[': ']', '{': '}'}

    for c in 
        if c in char_match:
            stack.append(c)
        else:
            if not stack or char_match[stack.pop()] != c:
                return False
    
    return not stack


def test_is_valid():
    s = "()"
    assert is_valid(s) is True
    
    s = "()[]{}"
    assert is_valid(s) is True

    s = "(]"
    assert is_valid(s) is False

def is_palindrome(text: str) -> bool:

    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]

# Example
print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
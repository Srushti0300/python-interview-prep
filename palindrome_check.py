def is_palindrome(s):
    left = 0                    # pointer at the start
    right = len(s) - 1          # pointer at the end

    while left < right:
        if s[left] != s[right]:
            return False         # mismatch found, not a palindrome
        left += 1
        right -= 1

    return True                  # all characters matched

print(is_palindrome("madam"))
print(is_palindrome("hello"))
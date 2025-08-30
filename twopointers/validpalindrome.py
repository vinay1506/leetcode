def is_palindrome(s: str) -> bool:
    left,right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
s ="vinay"
pa="sis"
print(is_palindrome(s))  # Output: False
print(is_palindrome(pa))  # Output: True
        



# string_operations.py

def reverse_string(s):
    return s[::-1]

def count_words(s):
    words = s.split()
    return len(words)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

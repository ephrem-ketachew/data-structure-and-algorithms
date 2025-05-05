# DLL Palindrome Checker ( Interview Question)
# Instructions
# Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

# For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

# If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.

# Method name:
# is_palindrome

def is_palindrome(dll):
    left = dll.head
    right = dll.tail
    while left != right or left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev

    return True
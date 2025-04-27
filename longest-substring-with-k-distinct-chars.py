def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    
    left = 0
    longest_substring_length = 0
    char_dict = {}
    
    for right in range(len(s)):
        char = s[right]
        char_dict[char] = char_dict.get(char, 0) + 1
        
        while len(char_dict) > k:
            left_char = s[left]
            char_dict[left_char] -= 1
            if char_dict[left_char] == 0:
                del char_dict[left_char]
            left += 1
        
        longest_substring_length = max(longest_substring_length, right - left + 1)
    
    return longest_substring_length


# def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
#     left = 0
#     longest_substring_length = 0
#     sliding_window = ''
#     unique_chars_in_window = 0
    
#     for right in range(len(s)):
#         if s[right] not in sliding_window:
#             unique_chars_in_window += 1
#         sliding_window = s[left:right + 1]
#         while unique_chars_in_window > k:
#             left += 1
#             sliding_window = s[left:right + 1]
#             unique_chars_in_window = len(set(sliding_window))
            
#         longest_substring_length = max(longest_substring_length, len(sliding_window))
            
#     return longest_substring_length

        
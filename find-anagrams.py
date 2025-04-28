from collections import Counter

def find_anagrams(s: str, p: str):
    output = []
    len_s = len(s)
    len_p = len(p)
    
    if len_s < len_p:
        return output
    
    p_counter = Counter(p)
    window_counter = Counter(s[:len_p])
    
    if p_counter == window_counter:
        output.append(0)
        
    for right in range(len_p, len_s):
        window_counter[s[right]] += 1
        window_counter[s[right - len_p]] -= 1
        
        if window_counter[s[right - len_p]] == 0:
            del window_counter[s[right - len_p]]
        
        if p_counter == window_counter:
            output.append(right - len_p + 1)
        
    return output
    

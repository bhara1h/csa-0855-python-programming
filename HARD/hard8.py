def is_scramble(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    
    n = len(s1)
    for i in range(1, n):
        if (is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])) or (is_scramble(s1[:i], s2[-i:]) and is_scramble(s1[i:], s2[:-i])):
            return True
    
    return False

# Test Cases
print(is_scramble("great", "eatgr"))  # Output: True
print(is_scramble("abcde", "caebd"))  # Output: False
print(is_scramble("a", "a"))          # Output: True
print(is_scramble("ab", "ad"))        # Output: False

def modify_string(S):
    # Calculate the frequency of each character
    frequency = {}
    for char in S:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Create the modified string
    modified_string = ""
    for char in S:
        freq = frequency[char]
        new_char = chr((ord(char) - ord('a') + freq) % 26 + ord('a'))
        modified_string += new_char
    
    return modified_string

# Test cases
print(modify_string("ghee"))     # Output: higg
print(modify_string("elephant")) # Output: flfsoibu
print(modify_string("apple"))    # Output: cqplf
print(modify_string("orange"))   # Output: ptbohf
print(modify_string("lion"))     # Output: mipo

def remove_common_words(S1, S2):
    # Split the sentences into words
    words1 = set(S1.split())
    words2 = set(S2.split())
    
    # Find common words
    common_words = words1.intersection(words2)
    
    # Remove common words from both sentences
    result1 = " ".join([word for word in S1.split() if word not in common_words])
    result2 = " ".join([word for word in S2.split() if word not in common_words])
    
    return result1, result2

# Test cases
S1 = "sky is blue in color"
S2 = "Raj likes sky blue color"
result1, result2 = remove_common_words(S1, S2)
print(result1)  # Output: is in
print(result2)  # Output: Raj likes 

# Test case 1
S1 = "learn python"
S2 = "python is easy to learn"
result1, result2 = remove_common_words(S1, S2)
print(result1)  # Output: 
print(result2)  # Output: is easy to

# Test case 2
S1 = "raju likes apple"
S2 = "apple is red in color"
result1, result2 = remove_common_words(S1, S2)
print(result1)  # Output: raju likes
print(result2)  # Output: is red in color

# Test case 3
S1 = "sita likes orange"
S2 = "orange is rich in anti-oxidents"
result1, result2 = remove_common_words(S1, S2)
print(result1)  # Output: sita likes
print(result2)  # Output: is rich in anti-oxidents

# Test case 4
S1 = "raj is travelling to Chennai in train"
S2 = "the rain will reach Chennai at 8 pm"
result1, result2 = remove_common_words(S1, S2)
print(result1)  # Output: raj is travelling to in train
print(result2)  # Output: the rain will reach at 8 pm

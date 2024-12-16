def reverse_words(s):
    # Split the string into words, removing leading/trailing and multiple spaces
    words = s.strip().split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the words with a single space
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Test Cases
print(reverse_words("the sky is blue"))    # Output: "blue is sky the"
print(reverse_words(" hello world "))      # Output: "world hello"
print(reverse_words("a good example"))     # Output: "example good a"
print(reverse_words("apple is red"))       # Output: "red is apple"
print(reverse_words("Red rose"))           # Output: "rose Red"

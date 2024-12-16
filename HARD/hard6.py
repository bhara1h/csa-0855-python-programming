from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        # Sort the string and use it as a key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    
    # Return the grouped anagrams
    return list(anagrams.values())

# Test Cases
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams([""]))                                   # Output: [[""]]
print(group_anagrams(["a"]))                                  # Output: [["a"]]
print(group_anagrams(["banana"]))                             # Output: [["banana"]]
print(group_anagrams(["12345"]))                              # Output: [["12345"]]

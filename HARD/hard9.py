def shuffle(l1, l2):
    shuffled_list = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        shuffled_list.append(l1[i])
        shuffled_list.append(l2[j])
        i += 1
        j += 1
    while i < len(l1):
        shuffled_list.append(l1[i])
        i += 1
    while j < len(l2):
        shuffled_list.append(l2[j])
        j += 1
    return shuffled_list

# Test Cases
l1 = [1, 3, 5]
l2 = [2, 4, 6, 8, 10]
print(shuffle(l1, l2))  # Output: [1, 2, 3, 4, 5, 6, 8, 10]

def max_guests(T, E, L):
    if T <= 0 or len(E) != len(L):
        return "Invalid input"

    current_guests = 0
    max_guests = 0

    for i in range(T):
        current_guests += E[i] - L[i]
        if current_guests > max_guests:
            max_guests = current_guests

    return max_guests

# Sample Input
T = 5
E = [7, 0, 5, 1, 3]
L = [1, 2, 1, 3, 4]
print(f"Maximum number of guests on cruise at an instance: {max_guests(T, E, L)}")  # Output: 8

# Test Cases
print(max_guests(-4, [1, 5, 9, 10], [0, 2, 3, 4]))  # Output: Invalid input
print(max_guests(0, [10, 2, 3, 4], [1234]))        # Output: Invalid input
print(max_guests(4, [12, 85], [100]))              # Output: Invalid input
print(max_guests(5, [42, 0, 35, 12, 15], [1, 2, 1, 3, 4]))  # Output: 89
print(max_guests(1, [12], [10]))                   # Output: 2

def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    current_h = 1
    clipboard = 1

    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
        current_h += clipboard
        operations += 1

    if current_h == n:
        return operations
    else:
        return 0

# Example usage
n = 9
print(minOperations(n))  # Output: 6

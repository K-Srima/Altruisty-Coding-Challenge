def find_two_unique_numbers(arr):
    xor_all = 0
    for num in arr:
        xor_all ^= num

    # Find a set bit (rightmost set bit)
    set_bit = xor_all & -xor_all

    num1, num2 = 0, 0
    for num in arr:
        if num & set_bit:
            num1 ^= num
        else:
            num2 ^= num

    return sorted([num1, num2])

# Example usage:
N = 2
arr = [1, 2, 3, 2, 1, 4]
print(find_two_unique_numbers(arr))  # Output: [3, 4]

N = 1
arr = [2, 1, 3, 2]
print(find_two_unique_numbers(arr))  

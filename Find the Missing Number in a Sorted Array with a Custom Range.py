"""You are given an array of positive numbers from n to m, such that all numbers from n to m are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution."""

def find_missing_number_in_range(nums, start, end):
    # Calculate the expected sum for the range from start to end
    expected_sum = (end * (end + 1)) // 2 - ((start - 1) * start) // 2

    # Calculate the actual sum of the numbers in the array
    actual_sum = sum(nums)

    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum


# Example usage:
nums = [30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]  # 32 is missing
start, end = 30, 45
missing_number = find_missing_number_in_range(nums, start, end)
print(f"The missing number is: {missing_number}")

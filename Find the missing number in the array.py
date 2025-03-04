"""You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution."""


def find_missing_number(nums):
    # Length of the array
    n = len(nums) + 1  # The actual length is 1 more than the number of elements in the array

    # Calculate the expected sum of the first n numbers
    expected_sum = n * (n + 1) // 2

    # Calculate the actual sum of the array
    actual_sum = sum(nums)

    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum


# Example usage:
nums = [1, 2, 4, 5, 6]  # 3 is missing
missing_number = find_missing_number(nums)
print(f"The missing number is: {missing_number}")


"""Runtime complexity: Linear, 
O(n)

Memory complexity: Constant, 
O(1)"""

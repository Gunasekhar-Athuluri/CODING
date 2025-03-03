"""Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not."""

def has_pair_with_sum(nums, target):
    # Create a set to store the numbers we've seen so far
    seen = set()

    # Iterate through the list of numbers
    for num in nums:
        # Calculate the complement (the value we need to find)
        complement = target - num

        # If the complement is already in the set, return True
        if complement in seen:
            return True

        # Add the current number to the set
        seen.add(num)

    # If no such pair is found, return False
    return False


# Example usage:
nums = [10, 15, 3, 7]
target = 17

if has_pair_with_sum(nums, target):
    print(f"There are two numbers in the list that sum up to {target}.")
else:
    print(f"No two numbers in the list sum up to {target}.")

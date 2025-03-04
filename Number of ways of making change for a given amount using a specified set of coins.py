"""Suppose we have coin denominations of [1, 2, 5] and the total amount is 7"""

def coin_change_ways(denominations, amount):
    # Initialize dp array with 0's, dp[i] will store the number of ways to make change for amount i
    dp = [0] * (amount + 1)
    
    # There is 1 way to make change for 0 amount (by not using any coins)
    dp[0] = 1
    
    # Iterate over each coin in denominations
    for coin in denominations:
        # Update dp array for each possible amount from coin to the target amount
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    # The last element in dp will give the number of ways to make change for the target amount
    return dp[amount]

# Example usage:
denominations = [1, 2, 5]
amount = 7
result = coin_change_ways(denominations, amount)
print(f"Number of ways to make change for amount {amount} is: {result}")



"""
Example Walkthrough:
For denominations [1, 2, 5] and an amount of 7, the DP table updates as follows:

Start with dp array: dp = [1, 0, 0, 0, 0, 0, 0, 0] (initially, there's 1 way to make 0 amount, and 0 ways to make any other amount).

Process coin 1:

Update dp[i] for i from 1 to 7:
dp[1] = dp[1] + dp[1 - 1] = 0 + 1 = 1
dp[2] = dp[2] + dp[2 - 1] = 0 + 1 = 1
dp[3] = dp[3] + dp[3 - 1] = 0 + 1 = 1
dp[4] = dp[4] + dp[4 - 1] = 0 + 1 = 1
dp[5] = dp[5] + dp[5 - 1] = 0 + 1 = 1
dp[6] = dp[6] + dp[6 - 1] = 0 + 1 = 1
dp[7] = dp[7] + dp[7 - 1] = 0 + 1 = 1
Updated dp: [1, 1, 1, 1, 1, 1, 1, 1]
Process coin 2:

Update dp[i] for i from 2 to 7:
dp[2] = dp[2] + dp[2 - 2] = 1 + 1 = 2
dp[3] = dp[3] + dp[3 - 2] = 1 + 1 = 2
dp[4] = dp[4] + dp[4 - 2] = 1 + 2 = 3
dp[5] = dp[5] + dp[5 - 2] = 1 + 2 = 3
dp[6] = dp[6] + dp[6 - 2] = 1 + 3 = 4
dp[7] = dp[7] + dp[7 - 2] = 1 + 4 = 5
Updated dp: [1, 1, 2, 2, 3, 3, 4, 5]
Process coin 5:

Update dp[i] for i from 5 to 7:
dp[5] = dp[5] + dp[5 - 5] = 3 + 1 = 4
dp[6] = dp[6] + dp[6 - 5] = 4 + 1 = 5
dp[7] = dp[7] + dp[7 - 5] = 5 + 1 = 6
Updated dp: [1, 1, 2, 2, 3, 4, 5, 6]
Result: The number of ways to make change for 7 is dp[7] = 6.
"""

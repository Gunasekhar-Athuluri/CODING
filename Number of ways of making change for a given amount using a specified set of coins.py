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

# Suppose you’re going camping. You have a knapsack that will hold
# 6 lb, and you can take the following items. Each has a value, and the
# higher the value, the more important the item is:
# • Water, 3 lb, 10
# • Book, 1 lb, 3
# • Food, 2 lb, 9
# • Jacket, 2 lb, 5
# • Camera, 1 lb, 6

def knapsack(capacity, weights, values):
    n = len(weights)
    # Create a 2D DP table with (n + 1) rows and (capacity + 1) columns, initialized to 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # TODO: Implement algorithm

    # Proceed with solving the problem (using dynamic programming or another approach)
    return dp[n][capacity]

# Initialize variables
capacity = 6  # Maximum weight the knapsack can carry
weights = [3, 1, 2, 2, 1]  # Item weights
values = [10, 3, 9, 5, 6]  # Item values
knapsack(capacity, weights, values)
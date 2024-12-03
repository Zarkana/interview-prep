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

    for i in range(1, n + 1):
        for w in range(capacity+1):
            # If the current items weight fits within the current knapsack capacity
            if weights[i - 1] <= w:
                # The item fits, choose whichever is bigger, the previous rows value, or the current item + the value from the previous row that fits within the remaining capacity
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            # Skip adding this item because it does not fit
            else:
                # Use the previous row's best
                dp[i][w] = dp[i-1][w]
            print_2d_array(dp)
    # Proceed with solving the problem (using dynamic programming or another approach)
    return dp[n][capacity]

def print_2d_array(arr):
    # Calculate the maximum width of each column
    col_widths = [max(len(str(cell)) for cell in column) for column in zip(*arr)]
    
    # Print each row with the appropriate column widths
    for row in arr:
        print(' '.join(f"{str(cell).rjust(col_widths[i])}" for i, cell in enumerate(row)))


# Initialize variables
capacity = 6  # Maximum weight the knapsack can carry
weights = [3, 1, 2, 2, 1]  # Item weights
values = [10, 3, 9, 5, 6]  # Item values
knapsack(capacity, weights, values)
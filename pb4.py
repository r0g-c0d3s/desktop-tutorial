class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value to weight ratio

def knapsack(weights, values, W):
    n = len(weights)
    items = [Item(values[i], weights[i]) for i in range(n)]

    # Sort items by value to weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    total_weight = 0

    for item in items:
        if total_weight + item.weight <= W:
            total_weight += item.weight
            total_value += item.value
        else:
            # Take the fraction of the remaining weight
            remaining_weight = W - total_weight
            total_value += item.value * (remaining_weight / item.weight)
            break  # The knapsack is full

    return total_value, total_weight

# Input handling
n = int(input("Enter the number of items: "))
weights = []
values = []

for i in range(n):
    weight, value = map(int, input(f"Enter weights and values for item {i + 1} (separated by space): ").split())
    weights.append(weight)
    values.append(value)

W = int(input("Enter the maximum weight capacity of the knapsack: "))
max_value, total_weight = knapsack(weights, values, W)

print(f"The maximum value that can be obtained is: {max_value:.2f} with total weight: {total_weight}")

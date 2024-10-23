def find_subsets_with_sum(nums, target_sum):
    def recursive(index, current_sum, current_subset):
        if current_sum == target_sum:
            subsets.append(list(current_subset))
            return
        if current_sum > target_sum or index == len(nums):
            return

        # Include the current number
        current_subset.add(nums[index])
        recursive(index + 1, current_sum + nums[index], current_subset)

        # Exclude the current number
        current_subset.remove(nums[index])
        recursive(index + 1, current_sum, current_subset)

    subsets = []
    recursive(0, 0, set())
    return subsets

elements = list(map(int, input("Enter the elements (separated by spaces): ").split()))
target_sum = int(input("Enter the target sum: "))
result = find_subsets_with_sum(elements, target_sum)

if result:
    print("Subsets with sum", target_sum, "found:")
    for subset in result:
        print(set(subset))
else:
    print("No subset found with sum", target_sum)

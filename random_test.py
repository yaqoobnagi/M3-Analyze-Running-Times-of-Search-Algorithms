import random
from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search

# create random array
arr = [random.randint(1,100) for _ in range(20)]

# choose target (50% chance to exist)
target = random.choice(arr) if random.random() < 0.5 else 999

arr.sort()

print("Array:", arr)
print("Target:", target)

print("\nRecursive Binary Search:")
print(recursive_binary_search(arr, target, 0, len(arr)-1))

print("\nIterative Binary Search:")
print(iterative_binary_search(arr, target))

print("\nSequential Search:")
print(sequential_search(arr, target))

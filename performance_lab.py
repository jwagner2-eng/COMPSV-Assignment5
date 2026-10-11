# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return max(counts, key=counts.get)

"""
Time and Space Analysis for problem 1:

- Best-case: O(n), because we go through the list to count each number.

- Worst-case: O(n) with normal dictionary performance, although
  severe hash collisions could make it slower.

- Average-case: O(n), because checking and updating the dictionary
  usually takes O(1) time per number.

- Space complexity: O(n), because we might need to store every
  number in the dictionary if they are all different.

- Why this approach? I used a dictionary because it makes it
  easy to count how many times each number appears.

- Could it be optimized? Sorting could use less extra memory
  in some cases, but would usually take O(n log n) time.

- Trade-offs: Using a dictionary takes more memory, but
  makes finding the most frequent number faster.
"""
# Test cases for Problem 1
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected: 3
print(most_frequent([5, 5, 5]))              # Expected: 5
print(most_frequent([1, 2, 3]))              # Any value is valid
print(most_frequent([]))                     # Expected: None
print(most_frequent([-1, -1, 2]))            # Expected: -1


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:

- Best-case: O(n), because we still check every number in the list.

- Worst-case: O(n) with normal set performance, although
  hash collisions could make it slower.

- Average-case: O(n), because checking and adding values to
  a set usually takes O(1) time per number.

- Space complexity: O(n), because the set and result list
  may need to store every number if they are all different.

- Why this approach? I used a set to keep track of numbers
  already seen and a list to keep them in their original order.

- Could it be optimized? Using only a list would save the
  separate set, but checking for duplicates would be slower.

- Trade-offs: The set uses extra memory, but makes checking
  for duplicates much faster.
"""
# Test cases for Problem 2
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Expected: [4, 5, 6, 7]
print(remove_duplicates([1, 2, 3]))           # Expected: [1, 2, 3]
print(remove_duplicates([]))                  # Expected: []
print(remove_duplicates([5, 5, 5]))           # Expected: [5]
print(remove_duplicates([-1, 2, -1, 3]))      # Expected: [-1, 2, 3]


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        needed = target - num

        if needed in seen:
            pairs.append((needed, num))

        seen.add(num)

    return pairs
"""
Time and Space Analysis for problem 3:

- Best-case: O(n), because the function checks every number
  in the list even if there are no matching pairs.

- Worst-case: O(n) with normal set performance, although
  hash collisions could make it slower.

- Average-case: O(n), because checking and adding numbers
  to a set usually takes O(1) time per number.

- Space complexity: O(n), because the set and list of pairs
  may grow as the number of inputs increases.

- Why this approach? I used a set because it makes it easy
  to check if the number needed to complete a pair exists.

- Could it be optimized? A nested loop would avoid the set,
  but would take O(n^2) time instead of O(n).

- Trade-offs: Using a set requires extra memory, but
  allows the function to find pairs much faster.
"""
# Test cases for Problem 3
print(find_pairs([1, 2, 3, 4], 5))       # Expected: [(2, 3), (1, 4)]
print(find_pairs([1, 2, 3], 10))         # Expected: []
print(find_pairs([], 5))                 # Expected: []
print(find_pairs([-3, -1, 1, 3], 0))     # Expected: [(-1, 1), (-3, 3)]
print(find_pairs([2, 4, 6, 8], 10))      # Expected: [(4, 6), (2, 8)]


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    size = 0
    items = [None] * capacity

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print("Resizing from", capacity, "to", new_capacity)

            new_items = [None] * new_capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            capacity = new_capacity

        items[size] = i
        size += 1

    return items[:size]
"""
Time and Space Analysis for problem 4:

- When do resizes happen? Resizing happens when the list is full.
  The capacity starts at 2 and doubles to 4, 8, 16, and so on.

- Worst-case for a single append: O(n), because resizing
  requires copying all existing items into a larger list.

- Amortized time per append: O(1), because most additions
  do not require resizing. The expensive copies happen
  only occasionally.

- Space complexity: O(n), because the list needs enough
  space to store all the items, including unused capacity.

- Why does doubling reduce the cost overall? Doubling gives
  the list more room each time it fills up. This means
  resizing happens less often as more items are added.

- Trade-offs: Doubling uses extra memory for empty spaces,
  but it reduces how often the list needs to be copied.
"""

# Test cases for Problem 4
print(add_n_items(6))   # Expected: [0, 1, 2, 3, 4, 5]
print(add_n_items(0))   # Expected: []
print(add_n_items(1))   # Expected: [0]
print(add_n_items(2))   # Expected: [0, 1]
print(add_n_items(5))   # Expected: [0, 1, 2, 3, 4]
# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0

    for num in nums:
        current_sum += num
        totals.append(current_sum)

    return totals

"""
Time and Space Analysis for problem 5:

- Best-case: O(n), because we go through each number in the list once.

- Worst-case: O(n), because the function still only needs to go through the list one time.

- Average-case: O(n), because each number is added to the running total once.

- Space complexity: O(n), because we create a new list to store all the running totals.

- Why this approach? I used a running sum because it is simple and avoids adding the same numbers multiple times.

- Could it be optimized? We could change the original list instead of making a new one, which would save memory.

- Trade-offs: Changing the original list would use less memory, but it would also change the input data.
"""
# Test cases for Problem 5
print(running_total([1, 2, 3, 4]))    # Expected: [1, 3, 6, 10]
print(running_total([]))              # Expected: []
print(running_total([5]))             # Expected: [5]
print(running_total([-1, 2, -3]))     # Expected: [-1, 1, -2]
print(running_total([0, 0, 0]))       # Expected: [0, 0, 0]

# Optimized version of Problem 5
# Optimized to use O(1) extra space by updating the original list.
def running_total_optimized(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums

"""
Optimization Comparison for Problem 5:

- Original version: O(n) time and O(n) extra space because
  it creates a separate list for the running totals.

- Optimized version: O(n) time and O(1) extra space because
  it updates the numbers in the original list.

- What improved? The optimized version uses less memory
  while keeping the same time complexity.

- Trade-offs: The optimized version changes the original
  list, while the first version leaves it unchanged.
"""

# Test cases for optimized Problem 5
print(running_total_optimized([1, 2, 3, 4]))  # Expected: [1, 3, 6, 10]
print(running_total_optimized([]))            # Expected: []
print(running_total_optimized([5]))           # Expected: [5]
print(running_total_optimized([-1, 2, -3]))   # Expected: [-1, 1, -2]
print(running_total_optimized([0, 0, 0]))     # Expected: [0, 0, 0]

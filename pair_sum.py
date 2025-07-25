def find_pair_with_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            print(f"Pair found ({complement}, {num})")
            return
        seen.add(num)
    print("Pair not found.")

# Example usage
find_pair_with_sum([8, 7, 2, 5, 3, 1], 10)
find_pair_with_sum([5, 2, 6, 8, 1, 9], 12)
find_pair_with_sum([1, 2, 3, 4, 5], 9)
find_pair_with_sum([10, 20, 30, 40, 50], 100)
find_pair_with_sum([-3, -1, 2, 5, 8], 7)


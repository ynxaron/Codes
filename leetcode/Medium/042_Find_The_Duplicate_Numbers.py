def find_the_duplicate_numbers(nums: list[int]) -> int:
    num_len = len(nums) - 1
    num_sum = (num_len * (num_len + 1)) // 2
    total_sum = sum(nums)
    return (total_sum - num_sum)

print(find_the_duplicate_numbers([3, 1, 3, 4, 2]))

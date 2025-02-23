def valid_anagrams(s1: str, s2: str) -> bool:
    s1_map, s2_map = {}, {}
    for c in s1:
        s1_map[c] = 1 + s1_map.get(c, 0)
    for c in s2:
        s2_map[c] = 1 + s2_map.get(c, 0)
    return s1_map == s2_map

def first_and_last(nums: list[int], target: int) -> list[int]:
    f, l = -1, -1
    for i in range(len(nums)):
        if nums[i] == target:
            if f == -1:
                f = i
            else:
                l = i
    return [f, l]

def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        if nums[m] > target:
            r = m - 1
    return -1

def kth_largest_elem(nums: list[int], k: int) -> int:
    bucket = [0] * (max(nums) + 1)
    for n in nums:
        bucket[n] += 1
    inx = 0
    for i in range(len(bucket) - 1, -1, -1):
        if inx + bucket[i] >= k:
            return i
        inx += bucket[i]
    return - 1

class Tree:
    def __init__(self, val: int):
        self.val   = val
        self.left  = None
        self.right = None

    def is_symetric(self) -> bool:
        left_val = self.left.val if self.left is not None else None
        right_val = self.right.val if self.right is not None else None

        if left_val is None and right_val is None:
            return True
        elif left_val is not None and right_val is not None:
            if left_val == right_val:
                return self.left.is_symetric() and self.right.is_symetric()
            else:
                return False
        return False

# Last updated: 22/06/2026, 15:50:18
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        indices = {}  # val -> index
4
5        for i, n in enumerate(nums):
6            indices[n] = i
7
8        for i, n in enumerate(nums):
9            diff = target - n
10            if diff in indices and indices[diff] != i:
11                return [i, indices[diff]]
12        return []
13        
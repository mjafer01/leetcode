# Last updated: 22/06/2026, 11:22:04
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_object = {}

        for num in nums:
            if num in num_object:
                return True

            num_object[num] = True

        return False
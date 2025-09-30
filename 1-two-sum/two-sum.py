class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in table:
                return [idx, table[diff]]
            table[num] = idx
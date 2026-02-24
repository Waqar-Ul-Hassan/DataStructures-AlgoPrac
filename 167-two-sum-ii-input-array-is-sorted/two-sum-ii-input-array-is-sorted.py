class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff = {}
        for n in range(len(numbers)):
            d = target - numbers[n]
            if d in diff:
                return [min(diff[d], n) + 1, max(diff[d], n)+1]
            diff[numbers[n]] = n
        
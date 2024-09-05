class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
            print(counter[n])
        

        vals = sorted(counter.values(), reverse=False)[len(counter)-k:]
        keys = [key for key, val in counter.items() if val in vals]
        return keys





        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for idx in strs:
            count = [0]*26

            for s in idx:
                count[ord(s) - ord("a")] += 1

            answer[tuple(count)].append(idx)
        
        return answer.values()
                
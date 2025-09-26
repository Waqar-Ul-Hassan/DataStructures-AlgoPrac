class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = {}
        table2 = {}

        for i in s:
            if i not in table1:
                table1[i] = 1
            table1[i] += 1
        
        for i in t:
            if i not in table2:
                table2[i] = 1
            table2[i] += 1

        return table1 == table2
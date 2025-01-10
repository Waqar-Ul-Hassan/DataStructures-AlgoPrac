class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0 or len(s) == 1:
            return s
        r = len(s)-1
        for l in range(len(s)):
            if l > r:
                return s
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            r-=1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_arr = list(str(x))
        
        r = len(x_arr)-1
        for l in range(len(x_arr)):
            if x_arr[l] != x_arr[r]:
                return False
            if l>=r:
                return True
            r-=1

class Solution:
    def romanToInt(self, s: str) -> int:
        arr = list(s)
        ans = 0
        i = 0
        while i < len(arr):
            if i!=len(arr)-1 and arr[i] == "I" and arr[i+1] == "V":
                ans+=4
                i+=2
                continue
            elif i!=len(arr)-1 and arr[i] == "I" and arr[i+1] == "X":
                ans+=9
                i+=2
                continue
            elif i!=len(arr)-1 and arr[i] == "X" and arr[i+1] == "L":
                ans+=40
                i+=2
                continue
            elif i!=len(arr)-1 and arr[i] == "X" and arr[i+1] == "C":
                ans+=90
                i+=2
                continue
            elif i!=len(arr)-1 and arr[i] == "C" and arr[i+1] == "D":
                ans+=400
                i+=2
                continue
            elif i!=len(arr)-1 and arr[i] == "C" and arr[i+1] == "M":
                ans+=900
                i+=2
                continue
            elif arr[i] == "I":
                ans+=1
                i+=1
                continue
            elif arr[i] == "V":
                ans+=5
                i+=1
                continue
            elif arr[i] == "X":
                ans+=10
                i+=1
                continue
            elif arr[i] == "L":
                ans+=50
                i+=1
                continue
            elif arr[i] == "C":
                ans+=100
                i+=1
                continue
            elif arr[i] == "D":
                ans+=500
                i+=1
                continue
            elif arr[i] == "M":
                ans+=1000
                i+=1
                continue
        return ans
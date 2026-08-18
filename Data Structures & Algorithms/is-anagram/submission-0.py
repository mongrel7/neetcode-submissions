class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        ans = {}
        for ch in s:
            ans[ch] = ans.get(ch,0) + 1
        for ch in t:
            if ch not in ans:
                return False 
            ans[ch] -= 1
            if(ans[ch] < 0):
                return False
        return True
        


        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {}
        z ={}

        for str in s:
            x[str] = x.get(str, 0) + 1
        
        for str in t:
            z[str] = z.get(str, 0) + 1
        
        if x == z:
            return True
        return False
            
        
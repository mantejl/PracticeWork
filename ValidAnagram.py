import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = collections.defaultdict(int)
        for c in s: 
            s_map[c] += 1
        
        for c in t: 
            if c not in s_map.keys():
                return False 
            else:
                s_map[c] -= 1

        for val in s_map.values():
            if val != 0: 
                return False 
        
        return True 
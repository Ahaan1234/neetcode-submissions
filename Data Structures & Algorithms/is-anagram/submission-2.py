class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s, seen_t = {}, {}
        for ch in s:
            seen_s[ch] = seen_s.setdefault(ch, 0)+1

        for ch in t:
            seen_t[ch] = seen_t.setdefault(ch, 0)+1

        print(seen_s)
        print(seen_t)
        
        if len(seen_s) != len(seen_t): return False
        for ch in seen_s:
            try:
                if seen_t[ch] != seen_s[ch]: return False
            except: return False
        
        return True
        

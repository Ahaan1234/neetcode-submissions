class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        s = s.lower()
        # print(s)
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue

            elif not s[j].isalnum():
                j -= 1
                continue
            
            if s[j] != s[i]:
                print(s[j])
                print(s[i])
                return False
            
            i += 1
            j -= 1
        
        return True

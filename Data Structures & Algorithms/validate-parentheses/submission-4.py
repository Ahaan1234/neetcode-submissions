class Solution:
    def isValid(self, s: str) -> bool:
        # naive: go step by step, remember open brackets, if closed bracket comes, check if last open is same as the close.
        # if not, false. 
        start = "([{"
        end = "}])"
        open_series = []
        for ch in s:
            if ch in start: 
                open_series.append(ch)
            else: 
                if len(open_series) == 0: return False
                if open_series[-1] == "(" and ch == ")":
                    open_series.pop()
                elif open_series[-1] == "[" and ch == "]":
                    open_series.pop()
                elif open_series[-1] == "{" and ch == "}":
                    open_series.pop()
                else: 
                    return False
                    
        if len(open_series) > 0: return False
        return True
class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0
        if len(s) == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        if s[0] == mn or s[-1] == mx:
            return 1
            
        has_mn_proper_prefix = any(c == mn for c in s[:-1])
        has_mx_proper_suffix = any(c == mx for c in s[1:])
        
        if not has_mn_proper_prefix and not has_mx_proper_suffix:
            return 3
            
        return 2
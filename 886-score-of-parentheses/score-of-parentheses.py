class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        cnt=0
        for ch in s:
            if ch=='(':
                stack.append(cnt)
                cnt=0
            else:
                cnt= stack.pop() + max(2 * cnt, 1)
        return cnt

        
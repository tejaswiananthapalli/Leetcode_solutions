class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def solve(s, open, close):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open < n:
                solve(s + "(", open + 1, close)

            if close < open:
                solve(s + ")", open, close + 1)

        solve("", 0, 0)
        return res
        
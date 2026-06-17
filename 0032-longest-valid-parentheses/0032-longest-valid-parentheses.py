class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                best = max(best, left * 2)
            elif right > left:
                left = right = 0

        left = right = 0
        for ch in reversed(s):
            if ch == ')':
                right += 1
            else:
                left += 1
            if left == right:
                best = max(best, left * 2)
            elif left > right:
                left = right = 0

        return best
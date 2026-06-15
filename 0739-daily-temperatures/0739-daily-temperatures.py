class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        pending = []

        for day, temp in enumerate(temperatures):
            while pending and temperatures[pending[-1]] < temp:
                prev = pending.pop()
                answer[prev] = day - prev
            pending.append(day)

        return answer
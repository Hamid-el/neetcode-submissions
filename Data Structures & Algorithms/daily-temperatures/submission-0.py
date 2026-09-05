class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, t in enumerate(temperatures):
                            # index of temp ([1]) on top of stack
            while stack and stack[-1][1] < t:
                prev_idx, _ = stack.pop()
                res[prev_idx] = index - prev_idx

            stack.append((index, t))

        return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in sorted(zip(position, speed), reverse=True)]
        stack = []
        for pos, speed in cars:
            time = (target - pos)/speed 
            # or if len(stack) >= 2 and stack[-1] <= stack[-2]:  stack.pop()
            if not stack or time > stack[-1]: # curr car is slower than last fleet, so it is its own fleet, ends more right in graph at target than another car crossing the same "street" and would arrive earlier
                stack.append(time)

        return len(stack)
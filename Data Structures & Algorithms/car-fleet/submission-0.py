class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        tmp = list(zip(position,speed))
        tmp.sort(reverse = True)
        for pos,speed in tmp:
            dis = target - pos
            time = dis/speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 
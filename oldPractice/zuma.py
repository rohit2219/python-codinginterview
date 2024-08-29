#https://leetcode.com/problems/zuma-game/discuss/192304/short-python-BFS-solution
import re
class Solution:
    def findMinStep(self, board, hand):
        seen = set()
        queue = [(board, hand)]
        while queue:
            state, balls = queue.pop(0)
            if not state:
                return len(hand) - len(balls)
            for ball in set(balls):
                print(ball,balls)
                tmp = balls.replace(ball, '', 1)
                for i in range(1, len(state) + 1):
                    if ball != state[i - 1]:
                        continue
                    new = state[:i] + ball + state[i:]
                    print('new:',new)
                    while len(new):
                        next = re.sub(r'B{3,}|G{3,}|R{3,}|W{3,}|Y{3,}', '', new)
                        if len(next) == len(new):
                            break
                        new = next
                    if new not in seen:
                        seen.add(new)
                        print('new after add:', new)

                        queue.append((new, tmp))
        return -1

x=Solution()
print(x.findMinStep("RBYYBBRRB", "YRBGB"))
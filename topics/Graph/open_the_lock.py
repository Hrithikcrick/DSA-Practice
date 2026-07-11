from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque()
        queue.append(["0000", 0])

        visited = set()
        visited.add("0000")

        while queue:
            current, moves = queue.popleft()

            if current == target:
                return moves

            for i in range(4):
                digit = int(current[i])

                for change in [1, -1]:
                    new_digit = (digit + change) % 10
                    new_state = current[:i] + str(new_digit) + current[i + 1:]

                    if new_state in dead or new_state in visited:
                        continue

                    visited.add(new_state)
                    queue.append([new_state, moves + 1])

        return -1

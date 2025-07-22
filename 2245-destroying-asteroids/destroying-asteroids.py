class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)
        for _ in range(len(asteroids)):
            val = heapq.heappop(asteroids)
            if val > mass:
                return False
            mass += val
        return True
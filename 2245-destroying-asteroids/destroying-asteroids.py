class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        curr_mass=mass
        for i in range(len(asteroids)):
            if asteroids[i]>curr_mass:
                return False
            else:
                curr_mass+=asteroids[i]
        return True
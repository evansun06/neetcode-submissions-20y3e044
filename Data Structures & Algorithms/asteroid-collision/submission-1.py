class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_asteroids = []
        left_asteroids = []

        for asteroid in asteroids:
            if asteroid > 0:
                right_asteroids.append(asteroid)
            else:
                while right_asteroids:
                    if right_asteroids[-1] < -asteroid:
                        right_asteroids.pop()
                    else:
                        if right_asteroids[-1] == -asteroid:
                            right_asteroids.pop()
                        break  # Left-moving asteroid is destroyed.
                else:
                    left_asteroids.append(asteroid)

        return left_asteroids + right_asteroids
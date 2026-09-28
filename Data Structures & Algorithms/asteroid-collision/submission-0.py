class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        we maintain a monotic stack of all astroids moving right.
        
        as we iterate on each asteroid, if the asteroid is moving left (-):
        - we pop all astroids on the stack that are <= the size of the astroid moving left
        - if we end up popping all the astroids on the stack, we append the astoid moving left to a list

        at the end we append the list of left astroids with the surviving stack of right astroids
        """

        right_asteroids = []
        left_asteroids = []

        for asteroid in asteroids:
            if asteroid > 0:
                right_asteroids.append(asteroid)
            else:
                exploded = False
                while len(right_asteroids) > 0:
                    if abs(asteroid) > abs(right_asteroids[-1]):
                        right_asteroids.pop()
                    elif abs(asteroid) == abs(right_asteroids[-1]):
                        right_asteroids.pop()
                        exploded = True
                        break
                    else:
                        exploded = True
                        break
                
                if not exploded and len(right_asteroids) == 0:
                    left_asteroids.append(asteroid)
        
        return left_asteroids + right_asteroids
                        

                
            
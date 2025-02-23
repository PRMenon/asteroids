import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_CD, ASTEROID_KILL_SCORE

class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.score = 0
        

    # in the player class
    def triangle(self) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.display) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        # Uncomment below to render the actual hitbox
        # pygame.draw.circle(screen, "Red", self.position, self.radius)

    def rotate(self, dt: int) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            if self.shot_timer <=0:
                self.shoot()
                self.shot_timer = PLAYER_SHOOT_CD

    def move(self, dt):
        self.position += (pygame.Vector2(0, 1)
                          .rotate(self.rotation)
                            * PLAYER_SPEED * dt)
        
    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)

    def update_score(self):
        self.score += ASTEROID_KILL_SCORE

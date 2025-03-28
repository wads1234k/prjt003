import pygame  # pygame 모듈을 import

class Brick:
    def __init__(self, x, y, width, height, color=(255, 100, 100)):  # Default color: light red
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hit = False

    def draw(self, surface):
        if not self.hit:
            pygame.draw.rect(surface, self.color, self.rect)

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect) and not self.hit:
            self.hit = True
            ball.dy *= -1  # Reverse ball direction
            return True
        return False
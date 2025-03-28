import pygame  # pygame 모듈을 import

class Paddle:
    def __init__(self, x, y, width, height, color=(0, 255, 0)):  # Default color: green
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 10
        self.color = color

    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

        # Keep the paddle within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > (800 - self.rect.width):  # Assuming screen width is 800
            self.rect.x = 800 - self.rect.width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # Draw the paddle
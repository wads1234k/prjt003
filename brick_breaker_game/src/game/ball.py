import pygame

class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.dx = speed  # Set horizontal speed
        self.dy = -speed  # Set vertical speed
        self.color = color

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for collision with the left or right wall
        if self.rect.left <= 0:  # Left wall
            self.dx = abs(self.dx)  # Ensure the ball moves right
        elif self.rect.right >= 800:  # Right wall
            self.dx = -abs(self.dx)  # Ensure the ball moves left

        # Check for collision with the top wall
        if self.rect.top <= 0:  # Top wall
            self.dy = abs(self.dy)  # Ensure the ball moves down

    def bounce(self):
        self.dy = -self.dy

    def is_out_of_bounds(self):
        return self.rect.bottom > 600  # Example: screen height is 600

    def reset(self):
        self.rect.x = 400 - self.rect.width // 2
        self.rect.y = 300 - self.rect.height // 2
        self.dx = abs(self.dx)  # Reset to positive horizontal speed
        self.dy = -abs(self.dy)  # Reset to negative vertical speed

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
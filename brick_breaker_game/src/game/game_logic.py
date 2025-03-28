import pygame
import sys
from .paddle import Paddle
from .ball import Ball
from .brick import Brick

class GameLogic:
    def __init__(self, screen, ball_speed=3, lives=3):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.score = 0
        self.lives = lives  # Set initial lives
        self.bricks = self.create_bricks()
        self.ball = Ball(self.screen_width // 2, self.screen_height // 2, 10, (255, 200, 100), ball_speed)  # Yellow-orange ball
        self.paddle = Paddle(self.screen_width // 2 - 50, self.screen_height - 30, 100, 10, (0, 255, 0))  # Green paddle
        self.bg_color = (220, 240, 255)  # Light sky blue background

    def create_bricks(self):
        # Define brick dimensions
        brick_width = 60
        brick_height = 20
        padding = 10
        bricks = []

        # Calculate the number of bricks that fit horizontally
        cols = (self.screen_width - padding) // (brick_width + padding)
        x_offset = (self.screen_width - (cols * (brick_width + padding))) // 2

        for row in range(5):  # Example: 5 rows of bricks
            for col in range(cols):
                x = x_offset + col * (brick_width + padding)
                y = row * (brick_height + padding)
                bricks.append(Brick(x, y, brick_width, brick_height))
        return bricks

    def update(self):
        # Handle user input
        self.handle_user_input()

        # Move the ball
        self.ball.move()

        # Check for collision with the paddle
        if self.check_collision(self.ball, self.paddle):
            self.ball.bounce()

        # Check for collision with bricks
        for brick in self.bricks[:]:
            if self.check_collision(self.ball, brick):
                self.ball.bounce()
                self.bricks.remove(brick)
                self.score += 1
                break  # Prevent multiple collisions in one frame

        # Check if all bricks are destroyed
        if not self.bricks:
            self.win_game()

        # Check if the ball is out of bounds
        if self.ball.is_out_of_bounds():
            self.lives -= 1
            if self.lives <= 0:
                self.game_over()
            else:
                self.ball.reset()

    def draw(self):
        # Clear the screen and draw all game elements
        self.screen.fill(self.bg_color)  # Use light sky blue background
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        self.display_score()
        self.display_lives()
        pygame.display.flip()  # Update the display

    def handle_user_input(self):
        # Handle user input for paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")  # Use the move method with "left"
        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")  # Use the move method with "right"

    def check_collision(self, obj1, obj2):
        # Simple AABB collision detection
        return obj1.rect.colliderect(obj2.rect)

    def display_score(self):
        # Display the current score on the screen
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))  # Black text
        self.screen.blit(score_text, (10, 10))

    def display_lives(self):
        # Display the remaining lives on the screen
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {self.lives}", True, (0, 0, 0))  # Black text
        self.screen.blit(lives_text, (10, 50))

    def win_game(self):
        # Display win message and exit
        font = pygame.font.Font(None, 72)
        win_text = font.render("You Win!", True, (0, 128, 0))  # Dark green text
        self.screen.fill(self.bg_color)  # Use light sky blue background
        self.screen.blit(win_text, (200, 250))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds
        pygame.quit()
        sys.exit()

    def game_over(self):
        # Display game over message and exit
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 69, 0))  # Bright orange-red text
        self.screen.fill(self.bg_color)  # Use light sky blue background
        self.screen.blit(game_over_text, (200, 250))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds
        pygame.quit()
        sys.exit()
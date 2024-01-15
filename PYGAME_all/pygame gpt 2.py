# Import modules
import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
GRAVITY = 0.5

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Simple Minecraft")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Create a list of blocks
blocks = []

# Create a class for blocks
class Block:
    def _init_(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        # Draw a rectangle on the screen
        pygame.draw.rect(screen, self.color, [self.x, self.y, BLOCK_SIZE, BLOCK_SIZE])

    def update(self):
        # Apply gravity to the block
        self.y += GRAVITY

        # Check if the block is touching the bottom or another block
        if self.y + BLOCK_SIZE > SCREEN_HEIGHT or self.is_colliding():
            # Stop the block from falling
            self.y -= GRAVITY

    def is_colliding(self):
        # Loop through all the blocks in the list
        for block in blocks:
            # Check if the block is not itself and is overlapping with another block
            if block != self and self.x < block.x + BLOCK_SIZE and self.x + BLOCK_SIZE > block.x and self.y < block.y + BLOCK_SIZE and self.y + BLOCK_SIZE > block.y:
                # Return True if there is a collision
                return True

        # Return False if there is no collision
        return False

# Create a class for the player
class Player:
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def draw(self):
        # Draw a circle on the screen
        pygame.draw.circle(screen, WHITE, [self.x, self.y], BLOCK_SIZE // 2)

    def update(self):
        # Apply gravity to the player
        self.vy += GRAVITY

        # Move the player horizontally
        self.x += self.vx

        # Check if the player is touching the left or right edge of the screen
        if self.x - BLOCK_SIZE // 2 < 0 or self.x + BLOCK_SIZE // 2 > SCREEN_WIDTH:
            # Reverse the horizontal velocity
            self.vx *= -1

        # Move the player vertically
        self.y += self.vy

        # Check if the player is touching the bottom or another block
        if self.y + BLOCK_SIZE // 2 > SCREEN_HEIGHT or self.is_colliding():
            # Stop the player from falling and allow jumping
            self.vy = 0
            self.can_jump = True

    def is_colliding(self):
        # Loop through all the blocks in the list
        for block in blocks:
            # Check if the player is overlapping with a block
            if self.x < block.x + BLOCK_SIZE and self.x > block.x and self.y < block.y + BLOCK_SIZE and self.y + BLOCK_SIZE // 2 > block.y:
                # Return True if there is a collision
                return True

        # Return False if there is no collision
        return False

    def jump(self):
        # Check if the player can jump
        if self.can_jump:
            # Set the vertical velocity to a negative value
            self.vy = -10

            # Prevent further jumping until landing
            self.can_jump = False

# Create an instance of the player class at the center of the screen
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Create some blocks at random positions and colors on the screen
for i in range(20):
    x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
    y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)
    color = random.choice([GREEN, BROWN, BLUE])
    block = Block(x, y, color)
    blocks.append(block)

# Create a boolean variable to control the main loop
running = True



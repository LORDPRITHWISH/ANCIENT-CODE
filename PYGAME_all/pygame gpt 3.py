# Import modules
import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Minecraft")

# Create the clock
clock = pygame.time.Clock()

# Create the player
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BLOCK_SIZE, BLOCK_SIZE)

# Create the inventory
inventory = {"dirt": 0, "grass": 0, "water": 0}

# Create the world
world = []
for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
    for y in range(0, SCREEN_HEIGHT - BLOCK_SIZE * 5, BLOCK_SIZE):
        # Randomly generate dirt or grass blocks
        block_type = random.choice(["dirt", "grass"])
        # Create a block object with its type and rect
        block = {"type": block_type, "rect": pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)}
        # Add the block to the world list
        world.append(block)

    # Generate water blocks at the bottom of the screen
    for y in range(SCREEN_HEIGHT - BLOCK_SIZE * 5, SCREEN_HEIGHT - BLOCK_SIZE * 3):
        block_type = "water"
        block = {"type": block_type, "rect": pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)}
        world.append(block)

    # Generate air blocks at the top of the screen
    for y in range(0, SCREEN_HEIGHT - BLOCK_SIZE * 7):
        block_type = "air"
        block = {"type": block_type, "rect": pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)}
        world.append(block)

# Create some animals and enemies
animals = []
enemies = []
for i in range(10):
    # Randomly generate an animal type (cow or sheep) and a position on the screen
    animal_type = random.choice(["cow", "sheep"])
    animal_x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
    animal_y = random.randint(SCREEN_HEIGHT - BLOCK_SIZE * 7 - BLOCK_SIZE * 2,
                              SCREEN_HEIGHT - BLOCK_SIZE * 5 - BLOCK_SIZE * 2)
    # Create an animal object with its type and rect
    animal = {"type": animal_type,
              "rect": pygame.Rect(animal_x,
                                  animal_y,
                                  BLOCK_SIZE * 2,
                                  BLOCK_SIZE * 2),
              "direction": random.choice([-1,
                                          +1])} # The direction of movement (-1 for left or +1 for right)
    # Add the animal to the animals list
    animals.append(animal)

    # Randomly generate an enemy type (zombie or skeleton) and a position on the screen
    enemy_type = random.choice(["zombie", "skeleton"])
    enemy_x = random.randint(0,
                             SCREEN_WIDTH - BLOCK_SIZE)
    enemy_y = random.randint(SCREEN_HEIGHT - BLOCK_SIZE * 7 - BLOCK_SIZE,
                             SCREEN_HEIGHT - BLOCK_SIZE * 5 - BLOCK_SIZE)
    # Create an enemy object with its type and rect
    enemy = {"type": enemy_type,
             "rect": pygame.Rect(enemy_x,
                                 enemy_y,
                                 BLOCK_SIZE,
                                 BLOCK_SIZE),
             "direction": random.choice([-1,
                                         +1])} # The direction of movement (-1 for left or +1 for right)
    # Add the enemy to the enemies list
    enemies.append(enemy)

# Load some images for the animals
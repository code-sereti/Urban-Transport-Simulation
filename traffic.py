import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Vehicle class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

        # Reset position if the vehicle moves off the screen
        if self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height


# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Urban Transportation Planning Simulation")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
vehicles = pygame.sprite.Group()

# Create vehicles
for _ in range(10):
    vehicle = Vehicle(RED, 20, 40, random.randint(1, 5))
    vehicle.rect.x = random.randint(0, WIDTH - vehicle.rect.width)
    vehicle.rect.y = random.randint(0, HEIGHT - vehicle.rect.height)
    all_sprites.add(vehicle)
    vehicles.add(vehicle)

# Simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Refresh display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

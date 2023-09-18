import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# Create the car sprite
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 100])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10

# Create the enemy car sprite
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = -100
        self.speed = random.randint(5, 10)
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
            self.rect.y = -100
            self.speed = random.randint(5, 10)
   
# Create the sprite groups
all_sprites = pygame.sprite.Group()
car_sprite = Car(SCREEN_WIDTH//2, SCREEN_HEIGHT-100)
all_sprites.add(car_sprite)
enemy_sprites = pygame.sprite.Group()

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    # Update the sprites
    all_sprites.update()
    
    # Add new enemy cars
    if len(enemy_sprites) < 5:
        enemy_sprite = EnemyCar()
        all_sprites.add(enemy_sprite)
        enemy_sprites.add(enemy_sprite)
        
    # Check for collisions
    if pygame.sprite.spritecollide(car_sprite, enemy_sprites, False):
        game_over = True
        
    # Draw the screen
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    
    # Set the frame rate
    clock.tick(60)

# Show the game over message.
font = pygame.font.Font(None, 50)
text = font.render("Game Over", True, WHITE)
text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for the user to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
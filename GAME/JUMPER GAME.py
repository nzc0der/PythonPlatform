import random
import pygame
import sys
import subprocess
import time

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

WIDTH, HEIGHT = 1200, 600   
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.DOUBLEBUF, vsync=1)
pygame.display.set_caption("Mini Platformer")

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)
RED = (255, 50, 50)

FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.load('/Users/noah-zipor/Downloads/Evening Light.mp3')
pygame.mixer.music.play(-1)

# Load jump sound
jump_sound = pygame.mixer.Sound('/Users/noah-zipor/Downloads/Jump Sound Effect.mp3')

player_width, player_height = 40, 60
player_speed = 5
player_vel_x = 0
player_vel_y = 0
GRAVITY = 0.5
JUMP_STRENGTH = -12.5

ground_height = 40
ground_y = HEIGHT - ground_height

levels = [
    [
        pygame.Rect(400, 450, 120, 20),
        pygame.Rect(600, 350, 150, 20),
        pygame.Rect(800, 250, 100, 20),
    ],
    [
        pygame.Rect(300, 500, 150, 20),
        pygame.Rect(550, 400, 100, 20),
        pygame.Rect(750, 300, 200, 20),
        pygame.Rect(950, 200, 40, 20),
    ],
    [
        pygame.Rect(200, 480, 100, 20),
        pygame.Rect(400, 420, 120, 20),
        pygame.Rect(600, 360, 100, 20),
        pygame.Rect(800, 300, 120, 20),
        pygame.Rect(1000, 250, 80, 20),
    ],
    [
        pygame.Rect(150, 500, 100, 20),
        pygame.Rect(350, 440, 100, 20),
        pygame.Rect(550, 380, 150, 20),
        pygame.Rect(750, 320, 100, 20),
        pygame.Rect(950, 260, 150, 20),
        pygame.Rect(1150, 200, 40, 20),
    ],
    [
        pygame.Rect(300, 470, 100, 20),
        pygame.Rect(500, 420, 150, 20),
        pygame.Rect(700, 370, 80, 20),
        pygame.Rect(900, 320, 120, 20),
        pygame.Rect(1100, 270, 80, 20),
    ],
]

current_level = 0
platforms = levels[current_level]

start_x, start_y = 100, HEIGHT - player_height - 40
player_x, player_y = start_x, start_y
on_ground = False

running = True
game_completed = False

EPSILON = 1
total_levels = len(levels)

class Enemy:
    def __init__(self, x, y, width, height, min_x, max_x, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_x = min_x
        self.max_x = max_x
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.min_x or self.rect.right >= self.max_x:
            self.speed = -self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

def spawn_enemies_for_level(level_platforms):
    enemies = []
    if level_platforms:
        sorted_platforms = sorted(level_platforms, key=lambda p: p.top)
        candidate_platforms = sorted_platforms[1:] if len(sorted_platforms) > 1 else []
        if candidate_platforms:
            chosen_platform = random.choice(candidate_platforms)
            enemy_y = chosen_platform.top - 40
            enemy_width, enemy_height = 40, 40
            min_x = chosen_platform.left
            max_x = chosen_platform.right
            start_x = min_x
            enemies.append(Enemy(start_x, enemy_y, enemy_width, enemy_height, min_x, max_x, 1))
    return enemies

enemies = spawn_enemies_for_level(platforms)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player_vel_x = 0
    if keys[pygame.K_LEFT]:
        player_vel_x = -player_speed
    if keys[pygame.K_RIGHT]:
        player_vel_x = player_speed

    if keys[pygame.K_UP] and on_ground:
        player_vel_y = JUMP_STRENGTH
        on_ground = False
        jump_sound.play()

    player_vel_y += GRAVITY

    last_platform = platforms[-1]
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    standing_on_last = (
        abs(player_rect.bottom - last_platform.top) <= EPSILON
        and player_rect.right > last_platform.left
        and player_rect.left < last_platform.right
    )

    next_rect = pygame.Rect(player_x + player_vel_x, player_y, player_width, player_height)
    collision = False
    for platform in platforms:
        if next_rect.colliderect(platform):
            collision = True
            break

    if standing_on_last:
        right_limit = WIDTH
    else:
        right_limit = last_platform.right

    if not collision and 0 <= next_rect.left and next_rect.right <= right_limit:
        player_x += player_vel_x
    else:
        player_vel_x = 0

    next_rect = pygame.Rect(player_x, player_y + player_vel_y, player_width, player_height)
    on_ground = False
    collided_vertically = False

    if next_rect.bottom >= ground_y:
        first_platform = platforms[0]
        touching_ground_right = player_x > first_platform.right
        falling_or_on_ground = player_vel_y >= 0
        if touching_ground_right and falling_or_on_ground:
            player_x, player_y = start_x, start_y
            player_vel_y = 0
            on_ground = False
        else:
            player_y = ground_y - player_height
            player_vel_y = 0
            on_ground = True
            collided_vertically = True
    else:
        on_platform = False
        for platform in platforms:
            if next_rect.colliderect(platform):
                if player_vel_y > 0:
                    player_y = platform.top - player_height
                    player_vel_y = 0
                    on_ground = True
                    collided_vertically = True
                    on_platform = True
                    break
                elif player_vel_y < 0:
                    player_y = platform.bottom
                    player_vel_y = 0
                    collided_vertically = True
                    break
        if not collided_vertically:
            player_y += player_vel_y
        if not on_platform and not collided_vertically:
            on_ground = False

    for enemy in enemies:
        enemy.update()
        if enemy.rect.colliderect(player_rect):
            player_x, player_y = start_x, start_y
            player_vel_y = 0
            on_ground = False

    if standing_on_last and keys[pygame.K_RIGHT] and player_x + player_width >= last_platform.right:
        current_level += 1
        if current_level >= total_levels:
            game_completed = True
            running = False
        else:
            platforms = levels[current_level]
            player_x, player_y = start_x, start_y
            player_vel_y = 0
            on_ground = False
            enemies = spawn_enemies_for_level(platforms)

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, ground_height))
    for platform in platforms:
        pygame.draw.rect(screen, BROWN, platform)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

if game_completed:
    pygame.mixer.music.fadeout(1000)
    time.sleep(1)

pygame.quit()

if game_completed:
    subprocess.run(["python3", "exit.py"])

sys.exit()

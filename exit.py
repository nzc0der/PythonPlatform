import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Finished!")

font = pygame.font.SysFont(None, 48)
text = font.render("You Finished The Game!", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()

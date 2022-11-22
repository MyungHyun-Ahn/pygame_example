import sys, pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill((255, 255, 255))
    #그리기 코드 입력
    for y in range(0, 300, 25):
        pygame.draw.line(SURFACE, (0, 0, 0), (0, y), (400, y))
    for x in range(0, 400, 25):
        pygame.draw.line(SURFACE, (0, 0, 0), (x, 0), (x, 300))
    pygame.display.update()
    FPSCLOCK.tick(3)
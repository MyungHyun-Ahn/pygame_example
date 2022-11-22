import random   # 추가해야 함
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
    
    pointlist = [] # 이을 점을 모을 리스트
    for _ in range(10):
        xpos = random.randint(0, 400)
        ypos = random.randint(0, 300)
        pointlist.append((xpos, ypos))

    pygame.draw.lines(SURFACE, (0,0,0), True, pointlist, 5)

    pygame.display.update()
    FPSCLOCK.tick(3)
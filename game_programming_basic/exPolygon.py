import random   # 추가해야 함
import sys, pygame
from pygame.locals import QUIT, Rect
from math import radians, cos, sin  # 추가해야 함
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill((255, 255, 255))
    
    pointlist0, pointlist1 = [], []
    for theta in range(0, 360, 20): # 360 / 5 = 72도 회전
        rad = radians(theta)
        pointlist0.append((cos(rad)*100 + 100, sin(rad)*100 + 150))
        pointlist1.append((cos(rad)*100 + 300, sin(rad)*100 + 150))

    pygame.draw.lines(SURFACE, (0,0,0), True, pointlist0) #기본 선굵기=1
    pygame.draw.polygon(SURFACE, (0,0,0), pointlist1) #선굵기 생략하면 채움

    pygame.display.update()
    FPSCLOCK.tick(3)
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
    # pygame.draw.rect(SURFACE,(0,0,255),(10,10,200,150))
    pygame.draw.rect(SURFACE, (255, 0, 0), (10, 20, 100, 50))
    pygame.draw.rect(SURFACE, (255, 0, 0), (150, 10, 100, 30), 3)
    pygame.draw.rect(SURFACE, (0, 255, 0), ((100, 80), (80, 50)))
    pygame.draw.circle(SURFACE, (255, 0, 0), (250, 150), 30)
    pygame.draw.circle(SURFACE, (0, 255, 0), (350, 200), 20)
    pygame.draw.ellipse(SURFACE, (255, 0, 0), (250, 80, 80, 30))
    # x, y, 위길이, 아래길이
    pygame.draw.ellipse(SURFACE, (0, 0, 0), (0, 0, 300, 300))
    # 중심좌표, 반지름
    pygame.draw.circle(SURFACE, (0, 0, 255), (150, 150), 150)
    # 시작점 끝점 굵기
    pygame.draw.line(SURFACE, (255, 0, 0), (10, 80), (200, 80), 15)
    pygame.display.update()
    FPSCLOCK.tick(3)
import sys, pygame
import random
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((300, 200))
FPSCLOCK = pygame.time.Clock()

def main():
    font = pygame.font.SysFont(None, 36)
    count = 100
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if count > 0:
            count -= 1
        SURFACE.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # font.render( 텍스트, antialias:윤곽선을 매끄럽게 설정, 글자 색상 )
        count_img= font.render("count {}".format(count),True,(0,0,0))
        SURFACE.blit(count_img, (100, 50))
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == "__main__":
    main()
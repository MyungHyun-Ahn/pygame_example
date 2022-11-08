"""
Cave 동굴 게임
 - 간단한 가로 스크롤 게임
 - 비행기는 스페이스를 누르면 위로 가속도가 붙음
 - 스페이스 키만 사용
 - 동굴은 점점 좁아짐
"""
"""
도전과제
1단계
 - 1000점 단위마다 배경색상 랜덤                           CLEAR
2단계
 - 상/하 화살표로 위아래 이동                              CLEAR
3단계
 - 최고 점수 (BEST SCORE)를 파일에 저장하여 표시           CLEAR
 - 게임을 다시 시작하면 최고 점수가 현재 점수와 함께 표시   CLEAR
4단계
 - 횡스크롤 게임을 종스크롤 방식으로 변환                  CLEAR
5단계
 - 동굴에 장애물(암석) 추가 장애물과 충돌하면 점수 감점     CLEAR
6단계
 - 동굴 변환에 삼각함수를 사용해서 매끄러운 동굴로 만든다   
7단계
 - 배경음악과 효과음을 추가한다.

"""
import sys
from random import randint
import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()

SAVEFILEPATH = "Cave/savefile.txt"

f1 = open(SAVEFILEPATH, 'r')
bestScore = f1.readline()
bestScore = int(bestScore)

f1.close()

def main():
    """ 메인 루틴 """
    walls = 80
    ship_x = 300
    velocity = 0
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("Cave/shipv.png")
    bang_image = pygame.image.load("Cave/bang.png")
    rock_image = pygame.image.load("Cave/rock.png")
    rock_y = 0
    rock_x = 300
    isCrash = False

    holes = []

    colorX = 0
    colorY = 255
    colorZ = 0

    for ypos in range(walls):
        holes.append(Rect(100, 600 - ypos * 10, 400, 10))
    game_over = False

    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
                if not game_over:
                    if event.key == K_LEFT:
                        ship_x -= 1
                    if event.key == K_RIGHT:
                        ship_x += 1
        
        # 내 캐릭터를 이동
        if not game_over:
            score += 10
            # velocity += -3 if is_space_down else 3
            ship_x += velocity

            # 동굴을 스크롤
            edge = holes[-1].copy()                              # 동굴을 이루는 오른쪽 끝 직사각형을 복사함
            test = edge.move(slope, 0)                         # slope 값만큼 위 아래로 조각을 이동함
            if test.left <= 0 or test.right >= 800:              # 동굴 조각이 화면 끝에 도달하면
                slope = randint(1, 6) * (-1 if slope > 0 else 1) # 방향과 값 수정함
                edge.inflate_ip(-20, 0)                          # 동굴 폭을 20만큼 감소시켜 동굴이 좁아짐
            edge.move_ip(slope, -10)                             # 오른쪽 끝 조각의 바로 오른쪽 위치로 이동시킴
            holes.append(edge)                                   # 맨 끝에 edge를 추가 (한조각이 더 많아짐)
            del holes[0]                                         # 맨 앞 직사각형을 삭제
            holes = [y.move(0, 10) for y in holes]              # 전체 조각을 왼쪽 방향으로 10만큼 이동

            # 충돌?
            if holes[0].left > ship_x or \
                holes[0].right < ship_x + 80:
                game_over = True
            
            rock_y += 10

            if rock_y >= 600:
                rock_y = 0
                rock_x = randint(holes[-1].left + 50, holes[-1].right - 50)
                isCrash = False
            
            if isCrash == False and rock_y > 510 and \
                (ship_x > rock_x - 60 and ship_x < rock_x + 60):
                score -= 100
                isCrash = True

        # 그리기
        if score % 1000 == 0:
            colorX = randint(0, 255)
            colorY = randint(0, 255)
            colorZ = randint(0, 255)

        SURFACE.fill((colorX, colorY, colorZ))

        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        SURFACE.blit(rock_image, (rock_x, rock_y))
        SURFACE.blit(ship_image, (ship_x, 510))
        score_image1 = sysfont.render("score : {}".format(score),
                                     True, (0, 0, 225))
        score_image2 = sysfont.render("best score : {}".format(bestScore),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image1, (600, 40))
        SURFACE.blit(score_image2, (600, 20))

        if isCrash:
            SURFACE.blit(bang_image, (ship_x-40, 510))

        if game_over:
            SURFACE.blit(bang_image, (ship_x-40, 510))
            f2 = open(SAVEFILEPATH, 'w')
            if bestScore < score:
                f2.write(str(score))
            else:
                f2.write(str(bestScore))
            f2.close()



        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()

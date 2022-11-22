"""
1단계 : 화면 확장 + 점수 표시 추가
        * 초록색 기본 아이템 먹을 때 마다 100점씩 증가
2단계 : 500점 단위로 속도가 5씩 증가 기본값은 5
3단계 : 노란색 스페셜 아이템 추가
        몸길이가 1로 줄어드는 아이템
4단계 : 파란색 스페셜 아이템 추가
        속도가 5로 초기화 되는 아이템
5단계 : 벽에 닿아도 죽지않고 반대 방향에서 나타나도록 수정

* 화면에 나타나는 아이템은 항상 10개
"""

import sys
import random
import pygame
from pygame.locals import QUIT, \
    KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode([1000, 600])
FPSCLOCK = pygame.time.Clock()

class Snake:
    """ Snake 객체 """
    bodies = []
    def __init__(self, pos):
        self.bodies = [pos]
        self.score = 0
        self.speed = 5
        self.isSpeedUp = False

    def move(self, key):
        """ Snake를 1프레임만큼 이동 """
        xpos, ypos = self.bodies[0]
        if key == K_LEFT:
            xpos -= 1
        elif key == K_RIGHT:
            xpos += 1
        elif key == K_UP:
            ypos -= 1
        elif key == K_DOWN:
            ypos += 1
        head = [xpos, ypos]
        

        if self.score != 0 and self.score % 500 == 0 and self.isSpeedUp == False:
            self.speed += 5
            self.isSpeedUp = True
            

        # 게임 오버 판정
        is_game_over = head in self.bodies 

        if head[0] >= W:
            head[0] = 0
        
        if head[0] < 0:
            head[0] = W - 1

        if head[1] >= H:
            head[1] = 0
        
        if head[1] < 0:
            head[1] = H - 1

        self.bodies.insert(0, head)
        foods = [FOODS[x][0:2] for x in range(len(FOODS))]
        if head in foods:
            # 먹이를 다른 장소로 이동
            i = foods.index(head)
            if FOODS[i][2] == (255, 212, 0):
                self.bodies = [self.bodies[0]]

            if FOODS[i][2] == (0, 0, 255):
                self.bodies.pop()
                self.speed = 5

            del FOODS[i]

            self.score += 100
            self.isSpeedUp = False

            add_food(self)
        else:
            self.bodies.pop()

        return is_game_over

    def draw(self):
        """ Snake를 그린다 """
        for body in self.bodies:
            pygame.draw.rect(SURFACE, (0, 255, 255),
                             Rect(body[0]*30, body[1]*30, 30, 30))

FOODS = []
(W, H) = (20, 20)

def add_food(snake):
    """ 임의의 장소에 먹이를 배치 """
    while True:
        pos = [random.randint(0, W-1), random.randint(0, H-1), random.choices([(0, 255, 0), (255, 212, 0), (0, 0, 255)], weights=[7, 2, 1])[0]]
        if pos in FOODS or pos in snake.bodies:
            continue
        FOODS.append(pos)
        break

def paint(snake, message, message1, message2):
    """ 화면 전체 그리기 """
    SURFACE.fill((0, 0, 0))
    pygame.draw.rect(SURFACE, (255, 255, 255), ((600, 0), (400, 600)))
    SURFACE.blit(message1, (610, 30))
    SURFACE.blit(message2, (610, 80))
    snake.draw()
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, food[2],
                            Rect(food[0]*30, food[1]*30, 30, 30))
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64),
                         (index*30, 0), (index*30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64),
                         (0, index*30), (600, index*30))
    if message != None:
        SURFACE.blit(message, (150, 300))
    pygame.display.update()

def main():
    """ 메인 루틴 """
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    snake = Snake((int(W/2), int(H/2)))
    for _ in range(10):
        add_food(snake)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        message1 = myfont.render("Score : {}".format(snake.score), True, (255, 212, 0))
        message2 = myfont.render("Speed : {}".format(snake.speed), True, (0, 0, 255))

        if game_over:
            message = myfont.render("Game Over!", True,
                                    (255, 255, 0))
        else:
            game_over = snake.move(key)

        paint(snake, message, message1, message2)
        FPSCLOCK.tick(snake.speed)

if __name__ == '__main__':
    main()
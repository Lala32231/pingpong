import pygame
pygame.init()
from time import time
from random import randint
from random import choice
FPS = 60
window = pygame.display.set_mode((500, 500))
dx = 3
dy = 3
win_width = 500
win_height = 700
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (500, 500))
clock = pygame.time.Clock()
player_group = pygame.sprite.Group()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = pygame.transform.scale(image, (w, h))
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed, up, down):
        super().__init__(x, y, w, h, image, speed)
        self.up = up
        self.down = down
        player_group.add(self)
    def move(self):
        k = pygame.key.get_pressed()
        if k[self.up]:
            print(2)
            if self.rect.top > 0:
                self.rect.y -= self.speed
        if k[self.down]:
            print(1)
            if self.rect.bottom < 500:
                self.rect.y += self.speed

    def collide(self, item):
        if self.rect.colliderect(item.rect):
            return True
        else:
            return False
class Ball(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image, speed)


ball_img = pygame.image.load('ball.png')
ball = Ball(100, 50, 40, 40, ball_img, 4)
player_img = pygame.image.load('player.png')
player = Player(0, 250, 20, 100, player_img, 4, pygame.K_w, pygame.K_s)
player2_img = pygame.image.load('player2.png')
player2 = Player(480, 250, 20, 100, player2_img, 4, pygame.K_UP, pygame.K_DOWN)
pygame.display.set_caption("Ping Pong")

score = 0
game = True
finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        if pygame.sprite.spritecollide(ball, player_group, False):
            dx *= -1
        player.draw()
        ball.draw()
        player.move()
        player2.draw()
        player2.move()
        ball.rect.x += dx
        ball.rect.y += dy
        if ball.rect.x > 430 or ball.rect.x < 0:
            dx *= -1
        if ball.rect.y > 430 or ball.rect.y < 0:
            dy *= -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and finish:   
            score = 0
            finish = False
    clock.tick(FPS)
    pygame.display.update()
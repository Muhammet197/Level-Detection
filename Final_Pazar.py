import pygame
import sys
import random

width = 800
height = 600

background = pygame.image.load("background.png") # kendi arkaplan resmimizi aynı dosyaya atıp adını buraya yazacağız
background = pygame.transform.scale(background,(width,height))

 

class Player(pygame.sprite.Sprite):
    def __init__(self,speed,move_up,move_down,move_right,move_left):
        super().__init__()
        self.image = pygame.image.load("ship.png") # kendi gemi veya araç resmimizi aynı dosyaya atıp adını buraya yazacağız
        self.image = pygame.transform.scale(self.image,(50,50)) # *
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = speed
        self.move_left = move_left 
        self.move_right = move_right 
        self.move_up = move_up 
        self.move_down = move_down
        
    def update(self):
        
        keys = pygame.key.get_pressed()
        if keys[self.move_left]: 
            self.rect.x -= self.speed
        if keys[self.move_right]:
            self.rect.x += self.speed
        if keys[self.move_up]:
            self.rect.y -= self.speed
        if keys[self.move_down]:
            self.rect.y += self.speed

class Monster(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("monsterShip.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.y += random.randint(1,3)
        if self.rect.y > height - 70:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.y -= 5 
        if self.rect.y < 10:
            self.kill()
pygame.init()

all_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()
bullets = pygame.sprite.Group()


player = Player(speed=5,move_down=pygame.K_DOWN,move_up=pygame.K_UP,move_left=pygame.K_LEFT,move_right=pygame.K_RIGHT) 
player2 = Player(speed=5,move_down=pygame.K_s,move_up=pygame.K_w,move_left=pygame.K_a,move_right=pygame.K_d)
all_sprites.add(player)
all_sprites.add(player2)

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
fps = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet1 = Bullet(player.rect.right,player.rect.top)
                bullet2 = Bullet(player.rect.left,player.rect.top)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
            elif event.key == pygame.K_v:
                bullet3 = Bullet(player2.rect.right,player2.rect.top)
                bullet4 = Bullet(player2.rect.left,player2.rect.top)
                all_sprites.add(bullet3)
                all_sprites.add(bullet4)
                bullets.add(bullet3)
                bullets.add(bullet4)
    if len(monsters)< 5 :
        monster = Monster(random.randint(0,width-50),0)
        all_sprites.add(monster)
        monsters.add(monster)

    # Monster nesnelerini vurduğumuzda gerçekleşcek olayın tanımı
    hits = pygame.sprite.groupcollide(bullets,monsters,True,True)
    
    all_sprites.update()
    screen.blit(background,(0,0))

    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
sys.exit()
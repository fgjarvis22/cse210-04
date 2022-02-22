

# VERY MUCH IN PROGRESS GAME


# import pygame module in this program 
import pygame, random, sys
  
pygame.init()

win = pygame.display.set_mode((800, 800))
  
pygame.display.set_caption("Greed")
  
x = 390
y = 700
width = 10
height = 10
vel = 3
run = True
score = 0
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def pos(self):
        self.rect.y = random.randrange(0, 790)
        self.rect.x = random.randrange(0, 790)

class Gem(Block):
    def pos(self):
        self.rect.y = random.randrange(0, 790)
        self.rect.x = random.randrange(0, 790)

class Player(Block):
    def update(self):
        self.rect.x = x
        self.rect.y = y

block_list = pygame.sprite.Group()
gem_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(20):
    block = Block((255,255,255), 10, 10)

    block.rect.x = random.randrange(0,790)
    block.rect.y = random.randrange(0,790)
 
    block_list.add(block)
    all_sprites_list.add(block)

for i in range(20):
    gem = Gem((0,0,255), 10, 10)

    gem.rect.x = random.randrange(0,790)
    gem.rect.y = random.randrange(0,790)
 
    gem_list.add(gem)
    all_sprites_list.add(gem)


player = Player((255,0,0),20,20)
all_sprites_list.add(player)

smallfont = pygame.font.SysFont('corbel',15)


while run:

    pygame.time.delay(10)
      
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
              
            run = False

    keys = pygame.key.get_pressed()
      
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<800-width:
        x += vel
    if keys[pygame.K_UP] and y>0:
        y -= vel
    if keys[pygame.K_DOWN] and y<800-height:
        y += vel

    win.fill((0, 0, 0))
    
    #arrowImg = pygame.image.load('arrow.png')
    #playerImg = pygame.transform.scale(arrowImg, (20,20))
    #arrow = pygame.sprite.Sprite()
    #arrow.image = playerImg.convert()
    #arrow.rect=arrow.image.get_rect()
    #arrow.rect.midbottom = [x,y]
    #win.blit(arrow.image,arrow.rect)
 

    #all_gems = pygame.sprite.group()
    #gemImg = pygame.image.load('gem.png')
    #gem = pygame.transform.scale(gemImg, (30, 30))
    all_sprites_list.update()
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    gem_hit_list = pygame.sprite.spritecollide(player, gem_list, False)

    for block in blocks_hit_list:
        score -=1
        block.pos()
    for gem in gem_hit_list:
        score +=1
        gem.pos()

    all_sprites_list.draw(win)

    text_score = smallfont.render(f'Score: {score}', True, (255,255,255))
    win.blit(text_score,(5,780))

    pygame.display.update() 

pygame.quit()

print(score)
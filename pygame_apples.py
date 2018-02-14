
import random, sys, pygame
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

screensize = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)
orange = (255,150,0)
red = (255,0,0)
pink = (255, 200, 200)
green = (0,255,0)
dark_green = (0,128,0)
yellow = (255,255,0)
purple = (150, 15, 150)
blue = (0, 40, 255)
indigo = (0, 0, 100)
colorP = (orange, green, purple, blue, indigo)
colorE = (red, pink, dark_green)

class Player():
    def __init__(self, initials, color, playerX = 393 , playerY = 293):
        self.initials = initials
        self.color = color
        self.playerX = playerX
        self.playerY = playerY

    def change_position(self, xPlus = 0, yPlus = 0):
        self.playerX += xPlus
        self.playerY += yPlus

class Banana():
    def __init__(self, bananaX, bananaY, size = (8,8)):
        self.bananaX = bananaX
        self.bananaY = bananaY
        self.size = size
    def new_loc(self):
        self.bananaX = random.randint(0,789)
        self.bananaY = random.randint(0,589)
    
def main():
    pygame.init()
    screen = pygame.display.set_mode(screensize)
    clock = pygame.time.Clock()
    player = Player("FOX", random.choice(colorP))
    font = pygame.font.SysFont("magneto", 32)
    points = 0
    
    fruit = Banana(random.randint(0,789), random.randint(0,589))
    
    pygame.key.set_repeat(1,1)

    (x,y) = (350, 20)
    
    
    while True:
        clock.tick(FPS)
        screen.fill(black)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_w] and player.playerY > 3:
                player.change_position(yPlus = -1)

            if keys[pygame.K_s] and player.playerY < 582:
                player.change_position(yPlus = 1)

            if keys[pygame.K_a] and player.playerX > 3:
                player.change_position(xPlus = -1)

            if keys[pygame.K_d] and player.playerX < 782:
                player.change_position(xPlus = 1)
        playerXRange = set(range(player.playerX, player.playerX + 15))
        playerYRange = set(range(player.playerY, player.playerY + 15))

        fruitXRange = set(range(fruit.bananaX, fruit.bananaX + 8))
        fruitYRange = set(range(fruit.bananaY, fruit.bananaY + 8))
        
        if playerXRange.intersection(fruitXRange) and playerYRange.intersection(fruitYRange):
            points += 10
            print(points)
            fruit.new_loc()
        dirty_rects = [pygame.Rect(350,20,50,50),pygame.Rect(player.playerX - 10, player.playerY - 10, 35, 35),pygame.Rect(fruit.bananaX - 10, fruit.bananaY - 10, 30, 30)]
        pygame.draw.rect(screen, player.color, (player.playerX, player.playerY, 15 ,15))
        pygame.draw.rect(screen, yellow, (fruit.bananaX, fruit.bananaY, 8, 8))

        text = str(points)
        f = font.render(text, True, white)
        (fwidth, fheight) = font.size(text)
        screen.blit(f,(x,y))
        
        pygame.display.update(dirty_rects)
            
        
if __name__ == '__main__':
    main()
    

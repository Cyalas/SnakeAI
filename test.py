import pygame


class cube:
    rows,width = 20,500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self):
        # for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        # for key in keys:
        if keys[pygame.K_LEFT]:
            self.dirnx, self.dirny = (-1,0)
        elif keys[pygame.K_RIGHT]:
            self.dirnx, self.dirny = (1,0)
        elif keys[pygame.K_UP]:
            self.dirnx, self.dirny = (0,-1)
        elif keys[pygame.K_DOWN]:
            self.dirnx, self.dirny = (0,1)
        else:
            self.dirnx, self.dirny = self.pos

        self.pos = (self.pos[0]+self.dirnx,self.pos[1]+self.dirny)

        # self.pos

    def draw(self,surface):
        dis = self.width // self.rows
        pygame.draw.rect(surface,self.color,(self.pos[0]*dis,self.pos[1]*dis,dis,dis))
        print(self.pos)






def drawGrid(width,rows,surface):
    sizeBtwn = width // rows
    x,y=0,0

    for l in range(rows):
        x = x+sizeBtwn
        y= y + sizeBtwn

        pygame.draw.line(surface,(255,255,255),(x,0),(x,width))
        pygame.draw.line(surface,(255,255,255),(0,y),(width,y))
        pygame.display.update()



def redrawWindow(surface):
    global rows, width, Mycube
    surface.fill((0,0,0))
    Mycube.draw(surface)
    drawGrid(width,rows,surface)




def main():

    global rows, width, Mycube
    rows, width = 20,500
    pygame.init()
    win = pygame.display.set_mode((width,width))
    green = (0,255,0)
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(15)
        Mycube = cube((1,0))
        Mycube.move()
        redrawWindow(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

#


main()

from pygame import *
from random import randint
import math
background= [44, 44, 44]
window = display.set_mode((1200, 700))
window.fill(background)
blocksList = []
randblocks = []
display.set_caption("Міни")
display.set_icon(transform.scale(image.load("icon.png"), (256, 256)))
clock = time.Clock()
LEFT = 1
RIGHT = 3

images = [transform.scale(image.load("empty.png"), (32, 32)), transform.scale(image.load("1.png"), (32, 32)), transform.scale(image.load("2.png"), (32, 32)), transform.scale(image.load("3.png"), (32, 32)), transform.scale(image.load("4.png"), (32, 32)), transform.scale(image.load("5.png"), (32, 32)),transform.scale(image.load("6.png"), (32, 32)), transform.scale(image.load("7.png"), (32, 32)), transform.scale(image.load("8.png"), (32, 32)), transform.scale(image.load("block.png"), (32, 32)), transform.scale(image.load("flag.png"), (32, 32)), transform.scale(image.load("bombhere.png"), (32, 32)), transform.scale(image.load("clickedbomb.png"), (32, 32)), transform.scale(image.load("hovered_block.png"), (32, 32))]
class Block(sprite.Sprite):
  # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, is_Bomb, is_open):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        # кожний спрайт повиннен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.is_bomb = is_Bomb
        self.is_open = is_open

        # кожний спрайт спрайт зберігає властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 

num = 0
blockGroup = sprite.Group()
for x in range(9):
    for y in range(9):
        num += 1
        blocksList.append(Block('block.png', (1200/2 - 144) + x * 32, (700/2 - 144) + y * 32, 32, 32, False, False))

for q in range(len(blocksList)):
    blocksList[q].num = q
    blocksList[q].x = int(q%math.sqrt(len(blocksList)))
    blocksList[q].y = int((q-q%math.sqrt(len(blocksList)))/math.sqrt(len(blocksList)))
def around(block):
    ab = []
    # a = blocksList.index(point)
    a = block.num
    X = blocksList[a].x
    Y = blocksList[a].y
    for i in range(len(blocksList)):
        for j in range(-1,2, 1):
            for k in range(-1,2, 1):
                if blocksList[i].x == X + j and blocksList[i].y == Y + k:
                    if j== 0 and k == 0:
                        pass
                    else:
                        ab.append(blocksList[i])
    return ab

for i in range(10):
    n = randint(0, 80)
    while n in randblocks:
        n = randint(0, 80)
    randblocks.append(n)
for g in range(len(blocksList)):
    if g in randblocks:
        blocksList[g].is_bomb = True
        # blocksList[g].image = transform.scale(image.load("bombhere.png"), (32,32))
for l in range(len(blocksList)):
    h = 0
    around(blocksList[l])
    for i in range(len(around(blocksList[l]))):
        if around(blocksList[l])[i].is_bomb:
            h+=1
    blocksList[l].bombnum = h
    if blocksList[l].is_bomb:
        pass
    else:
        pass
        # blocksList[l].image = images[h]
for a in range(len(blocksList)):
    blockGroup.add(blocksList[a])
def end():
    global finish
    finish = True
def openall(arc, num1):
    global finish
    if num1 == None:
        for t in range(len(blocksList)):
            if blocksList[t].num in randblocks:
                blocksList[t].image = images[11]     
    else:
        for t in range(len(blocksList)):
            if blocksList[t].num in randblocks:
                blocksList[t].image = images[11]
                blocksList[num1].image = images[arc]   
                end()
def flag():
    index2 = clicked_sprites2[0].num
    if blocksList[index2].is_open == True:
        pass
    else:
        if blocksList[index2].image == images[10]:
            blocksList[index2].image = images[9]
        else:
            blocksList[index2].image = images[10]
def checkisopen():
    p = 0
    for x in range(len(blocksList)):
        if blocksList[x].is_open:
            p+= 1
    if p == len(blocksList) - 10:
        openall(11, None)
def openblock():
    global finish
    index1 = clicked_sprites[0].num
    if blocksList[index1].is_bomb:
        openall(12, index1)

    elif blocksList[index1].bombnum:
        blocksList[index1].image = images[blocksList[index1].bombnum]
        blocksList[index1].is_open = True
    else:
        blocksList[index1].image = images[0]
        blocksList[index1].is_open = True
        openMoreBlocks(blocksList[index1])
    checkisopen()
def openMoreBlocks(a):
    b = around(a)
    for i in range(len(b)):
        c = b[i].num
        if blocksList[c].is_bomb or blocksList[c].is_open:
            pass
        else:
            if blocksList[c].bombnum:
                blocksList[c].is_open = True
                blocksList[c].image = images[blocksList[c].bombnum]
                
            else:
                blocksList[c].is_open = True
                blocksList[c].image = images[blocksList[c].bombnum]
                repeat(blocksList[c])
def repeat(a):
    openMoreBlocks(a)

global finish
finish = False
game = True

frame_count = 0
frame_rate = 60

while game:

    event1 = event.poll()
    for e in event.get():
        if e.type == QUIT:
            game = False
           
    blockGroup.draw(window)

    blockGroup.update(window)
    if not finish:
        if event1.type == MOUSEBUTTONDOWN and event1.button == LEFT:
            pos = mouse.get_pos()
            if pos[0] < (1200/2 - 144) or pos[0] > (1200/2 - 144) + 288:
                pass
            elif pos[1] < (700/2 - 144) or pos[1] > (700/2 - 144) + 288:
                pass
            else:
                clicked_sprites = [s for s in blocksList if s.rect.collidepoint(pos)]
                openblock()
        if event1.type == MOUSEBUTTONDOWN and event1.button == RIGHT:
            pos = mouse.get_pos()
            if pos[0] < (1200/2 - 144) or pos[0] > (1200/2 - 144) + 288:
                pass
            elif pos[1] < (700/2 - 144) or pos[1] > (700/2 - 144) + 288:
                pass
            else:
                clicked_sprites2 = [s for s in blocksList if s.rect.collidepoint(pos)]
                flag()
    clock.tick(frame_rate)
            

    display.update()
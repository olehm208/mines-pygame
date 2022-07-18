from pygame import *
from random import randint
import math
import os


blockSide = 16
bombnum = 40
background= [44, 44, 44]
window = display.set_mode((1200, 700))
minutes = 0
start_ticks = time.get_ticks()
blocksList = []
randblocks = []

os.chdir(os.getcwd() + "/data/")

display.set_caption("Міни")
display.set_icon(transform.scale(image.load("icon.png"), (256, 256)))
clock = time.Clock()
LEFT = 1
RIGHT = 3

font.init()
font1 = font.Font("Ubuntu-Light.ttf", 32)

current_flag_num = 0
max_flag_num = bombnum


images = [transform.scale(image.load("empty.png"), (32, 32)), transform.scale(image.load("1.png"), (32, 32)), transform.scale(image.load("2.png"), (32, 32)), transform.scale(image.load("3.png"), (32, 32)), transform.scale(image.load("4.png"), (32, 32)), transform.scale(image.load("5.png"), (32, 32)),transform.scale(image.load("6.png"), (32, 32)), transform.scale(image.load("7.png"), (32, 32)), transform.scale(image.load("8.png"), (32, 32)), transform.scale(image.load("block.png"), (32, 32)), transform.scale(image.load("flag.png"), (32, 32)), transform.scale(image.load("bombhere.png"), (32, 32)), transform.scale(image.load("clickedbomb.png"), (32, 32)), transform.scale(image.load("hovered_block.png"), (32, 32)), transform.scale(image.load("flagicon.png"), (32, 32))]
class Block(sprite.Sprite):
  # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, is_Bomb, is_open, is_flag):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        # кожний спрайт повиннен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.is_bomb = is_Bomb
        self.is_open = is_open
        self.is_flag = is_flag

        # кожний спрайт спрайт зберігає властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
gui_icons = sprite.Group()
flag_icon = Block('flagicon.png', 1006, 86, 32, 32, False, False, False)
clock_icon = Block('timer_icon.png', 1004, 184, 32, 32, False, False, False)
gui_icons.add(flag_icon)
gui_icons.add (clock_icon)
num = 0
blockGroup = sprite.Group()
for x in range(blockSide):
    for y in range(blockSide):
        num += 1
        blocksList.append(Block('block.png', ((1200 - (blockSide * 32))/2) + x * 32, ((700 - (blockSide * 32))/2) + y * 32, 32, 32, False, False, False))
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
for i in range(bombnum):
    n = randint(0, blockSide**2-1)
    while n in randblocks:
        n = randint(0, blockSide**2-1)
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
def timer123():
    global sec, minutes
    if sec >=60:
        minutes += 1
        sec = 0
    else:
        sec +=1
def end(endtype):
    global finish
    finish = True
    if not endtype:
        print("Lose")
    if endtype:
        print("Win")

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
                end(False)
def flag():
    global current_flag_num
    index2 = clicked_sprites2[0].num
    if blocksList[index2].is_open == True:
        pass
    else:
        if blocksList[index2].image == images[10]:
            blocksList[index2].is_flag = False
            blocksList[index2].image = images[9]
            current_flag_num -=1
        else:
            if current_flag_num < max_flag_num:
                blocksList[index2].is_flag = True
                blocksList[index2].image = images[10]
                current_flag_num +=1
            else:
                pass
def hover():
    for y in range(len(blocksList)):
        if blocksList[y].is_open == False:
            if blocksList[y].image != images[10]:
                blocksList[y].image = images[9]
            else:
                pass
        else:
            pass
    try:
        index3 = hovered_sprites[0].num
        if blocksList[index3].is_open:
            pass
        else:
            if blocksList[index3].image == images[10]:
                pass
            if blocksList[index3].image == images[9]:
                blocksList[index3].image = images[13]
    except IndexError:
        print(hovered_sprites)
        
def checkisopen():
    p = 0
    for x in range(len(blocksList)):
        if blocksList[x].is_open:
            p+= 1
    if p == len(blocksList) - bombnum:
        openall(11, None)
        end(True)
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

while game:

    window.fill(background)
    event1 = event.poll()
    for e in event.get():
        if e.type == QUIT:
            game = False

    blockGroup.draw(window)
    flag_txt = font1.render(f"{current_flag_num}/{max_flag_num}", 1, (255,255,255))
    gui_icons.draw(window)
    window.blit(flag_txt, (1048, 84))


    blockGroup.update(window)
    if not finish:
        print(mouse.get_pos())
        sec = (time.get_ticks() - start_ticks) / 1000
        timer123()
        if event1.type == MOUSEMOTION:
            pos = mouse.get_pos()
            
            if pos[0] < ((1200 - (blockSide * 32))/2) or pos[0] >= ((1200 - (blockSide * 32))/2) + blockSide*32:
                pass
            elif pos[1] < ((700 - (blockSide * 32))/2) or pos[1] >= ((700 - (blockSide * 32))/2) + blockSide*32:
                pass
            else:   
                hovered_sprites = [s for s in blocksList if s.rect.collidepoint(pos)]
                hover()
        if event1.type == MOUSEBUTTONDOWN and event1.button == LEFT:
            pos = mouse.get_pos()
            if pos[0] < ((1200 - (blockSide * 32))/2) or pos[0] >= ((1200 - (blockSide * 32))/2) + blockSide*32:
                pass
            elif pos[1] < ((700 - (blockSide * 32))/2) or pos[1] >= ((700 - (blockSide * 32))/2) + blockSide*32:
                pass
            else:
                clicked_sprites = [s for s in blocksList if s.rect.collidepoint(pos)]
                openblock()
        if event1.type == MOUSEBUTTONDOWN and event1.button == RIGHT:
            pos = mouse.get_pos()
            if pos[0] < ((1200 - (blockSide * 32))/2) or pos[0] >= ((1200 - (blockSide * 32))/2) + blockSide*32:
                pass
            elif pos[1] < ((700 - (blockSide * 32))/2) or pos[1] >= ((700 - (blockSide * 32))/2) + blockSide*32:
                pass
            else:
                clicked_sprites2 = [s for s in blocksList if s.rect.collidepoint(pos)]
                flag()
    timer = font1.render(f"{minutes:02d}:{int(sec):02d}", 1, (255,255,255))
    window.blit(timer, (1048, 184))
    display.update()

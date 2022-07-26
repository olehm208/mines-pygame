from pygame import *
from random import randint
from tkinter import *
from tkinter import messagebox
import os
import math
Tk().wm_withdraw()
class Options():
    def __init__(self, width,height,mines):
        self.width = width
        self.height = height
        self.mines = mines
optionList = [Options(9,9,10), Options(16,16,40), Options(30,16,99), Options(0,0,0)]
finish = True
game = True

background= [44, 44, 44]
window = display.set_mode((1200, 700),DOUBLEBUF,16)
minutes = 0
blocksList = []
randblocks = []

os.chdir(os.getcwd() + "/data/")

display.set_caption("Mines")
display.set_icon(transform.scale(image.load("icon.png"), (256, 256)))
clock = time.Clock()
LEFT = 1
RIGHT = 3

font.init()
font1 = font.Font("Ubuntu-Light.ttf", 32)
font1_bold = font.Font("Ubuntu-Light.ttf", 32)
font1_bold.set_bold(True)
font2 = font.Font("Ubuntu-Light.ttf", 24)




images = [transform.scale(image.load("empty.png").convert(), (32, 32)), transform.scale(image.load("1.png").convert(), (32, 32)), transform.scale(image.load("2.png").convert(), (32, 32)), transform.scale(image.load("3.png").convert(), (32, 32)), transform.scale(image.load("4.png").convert(), (32, 32)), transform.scale(image.load("5.png").convert(), (32, 32)),transform.scale(image.load("6.png").convert(), (32, 32)), transform.scale(image.load("7.png").convert(), (32, 32)), transform.scale(image.load("8.png").convert(), (32, 32)), transform.scale(image.load("block.png").convert(), (32, 32)), transform.scale(image.load("flag.png").convert(), (32, 32)), transform.scale(image.load("bombhere.png").convert(), (32, 32)), transform.scale(image.load("clickedbomb.png").convert(), (32, 32)), transform.scale(image.load("hovered_block.png").convert(), (32, 32)), transform.scale(image.load("flagicon.png").convert(), (32, 32))]
class Block(sprite.Sprite):
  # конструктор класу
    def __init__(self, block_image, block_x, block_y, size_x, size_y, is_Bomb, is_open, is_flag):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(block_image), (size_x, size_y))
        self.is_bomb = is_Bomb
        self.is_open = is_open
        self.is_flag = is_flag

        self.rect = self.image.get_rect()
        self.rect.x = block_x
        self.rect.y = block_y
        # self.around = around(self)
gui_icons = sprite.Group()
finish_buttons = sprite.Group()
flag_icon = Block('flagicon.png', 355, 25, 32, 32, False, False, False)
clock_icon = Block('timer_icon.png', 718, 25, 32, 32, False, False, False)
easy_button = Block('button.png', window.get_width()/2-235, 106,233, 233, False, False, False)
medium_button = Block('button.png', window.get_width()/2+3, 106,233, 233, False, False, False)
hard_button = Block('button.png', window.get_width()/2-235, 345,233, 233, False, False, False)
custom_button = Block('button.png', window.get_width()/2+3, 345,233, 233, False, False, False)
menu_btn = Block("button_hovered.png", 327, 632, 170, 60, False, False, False)
restart_button = Block("button_hovered.png", 635, 632, 170, 60, False, False, False)

gui_list = [easy_button, medium_button, hard_button, custom_button]
guiGroup = sprite.Group()
def bringbacksprites():
    global stop_bliting
    gui_icons.add(flag_icon)
    gui_icons.add (clock_icon)
    guiGroup.add(easy_button)
    guiGroup.add(medium_button)
    guiGroup.add(hard_button)
    guiGroup.add(custom_button)
    finish_buttons.add(restart_button)
    finish_buttons.add(menu_btn)
    stop_bliting = False
bringbacksprites()
num = 0
blockGroup = sprite.Group()

    
def around(block):
    ab = []
    # a = block.num
    X = block.x
    Y = block.y
    for i in range(len(blocksList)):
        for j in range(-1,2, 1):
            for k in range(-1,2, 1):
                if blocksList[i].x == X + j and blocksList[i].y == Y + k:
                    if j== 0 and k == 0:
                        pass
                    else:
                        ab.append(blocksList[i])
    return ab
def timer123():
    global sec, minutes
    if sec%60==59:
        minutes += 1   
    sec +=1
def end(endtype):
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
        pass
        
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
    elif blocksList[index1].image == images[10]:
        pass
    else:
        blocksList[index1].image = images[0]
        blocksList[index1].is_open = True
        openMoreBlocks(blocksList[index1])
    checkisopen()
    
def openMoreBlocks(a):
    b = around(a)
    for i in range(len(b)):
        c = b[i].num
        if blocksList[c].is_bomb or blocksList[c].is_open or blocksList[c].image == images[10]:
            pass
        else:
            if blocksList[c].bombnum:
                blocksList[c].is_open = True
                blocksList[c].image = images[blocksList[c].bombnum]
                
            else:
                blocksList[c].is_open = True
                blocksList[c].image = images[blocksList[c].bombnum]
                openMoreBlocks(blocksList[c])

def build(fieldHeight, fieldWidth):
    for y in range(fieldHeight):
        for x in range(fieldWidth):
            block = Block('block.png', ((1200 - (fieldWidth * 32))/2) + x * 32, ((700 - (fieldHeight * 32))/2) + y * 32, 32, 32, False, False, False)
            block.num = x+y*fieldWidth
            block.x = x
            block.y = y
            blocksList.append(block)
    for i in range(bombnum):
        n = randint(0, fieldHeight*fieldWidth-1)
        while n in randblocks:
            n = randint(0, fieldHeight*fieldWidth-1)
        randblocks.append(n)
    for g in range(len(blocksList)):
        if g in randblocks:
            blocksList[g].is_bomb = True
    for l in range(len(blocksList)):
        blocksList[l].around = around(blocksList[l])
        h = 0
        for i in range(len(blocksList[l].around)):
            if blocksList[l].around[i].is_bomb:
                h+=1
        blocksList[l].bombnum = h
    for a in range(len(blocksList)):
        blockGroup.add(blocksList[a])
stop_bliting = False
current_settings = 0
def restart():
    global finish
    finish = False
    for i in range(len(blocksList)):
        blockGroup.remove(blocksList[i])
    blocksList.clear()
    randblocks.clear()
    start(current_settings)
def buttons(current):
    global stop_bliting, current_settings
    medium_button.kill()
    easy_button.kill()
    hard_button.kill()
    custom_button.kill()
    window.fill(background)
    stop_bliting = True
    current_settings = current
    start(current)
def menu():
    global finish
    finish = True
    for i in range(len(blocksList)):
        blockGroup.remove(blocksList[i])
    blocksList.clear()
    randblocks.clear()
    bringbacksprites()
    start(3)

def start(index):
    global current_settings, fieldHeight, fieldWidth, bombnum, finish, game, current_flag_num, max_flag_num, flag_txt, sec, clicked_sprites, clicked_sprites2, hovered_sprites, stop_bliting, optionList
    fieldHeight = optionList[index].height
    fieldWidth = optionList[index].width
    bombnum = optionList[index].mines
    finish = False
    game = True
    current_flag_num = 0
    max_flag_num = bombnum

    build(fieldHeight, fieldWidth)
    start_ticks = time.get_ticks()
    while game:
        window.fill(background)
        event1 = event.poll()
        for e in event.get():
            if e.type == QUIT:
                game = False
        easy_txt = font1_bold.render("9x9", 1, (255,255,255))
        medium_txt = font1_bold.render("16x16", 1, (255,255,255))
        hard_txt = font1_bold.render("30x16", 1, (255,255,255))
        cust = font1_bold.render("Custom",1,(255,255,255))
        
        
        blockGroup.draw(window)
        guiGroup.draw(window)
        if stop_bliting:
            pass
        else:
            window.blit(easy_txt, (window.get_width()/2-147, 190))
            window.blit(medium_txt, (window.get_width()/2+67, 190))
            window.blit(hard_txt, (window.get_width()/2-170, 423))
            window.blit(cust, (window.get_width()/2+67, 423))
        if not easy_button.alive() or not medium_button.alive() or not hard_button.alive() or not custom_button.alive():
            sec = (time.get_ticks() - start_ticks) / 1000
            timer123()
        if finish:
            finish_buttons.draw(window)
            menu_txt = font1.render("Menu", 1, (255,255,255))
            restart_txt = font1.render("Restart", 1, (255,255,255))
            window.blit(menu_txt, (373, 644))
            window.blit(restart_txt, (670, 644))
        blockGroup.update(window)
        if event1.type == MOUSEBUTTONDOWN and event1.button == LEFT:
            pos = mouse.get_pos()
            if restart_button.alive():
                if restart_button.rect.collidepoint(pos):
                    restart()
            if menu_btn.alive():
                if menu_btn.rect.collidepoint(pos):
                    menu()
            if easy_button.alive():
                if easy_button.rect.collidepoint(pos):
                    buttons(0)
            if medium_button.alive():
                if medium_button.rect.collidepoint(pos):
                    buttons(1)
            if hard_button.alive():
                if hard_button.rect.collidepoint(pos):
                    buttons(2)
            if custom_button.alive():
                if custom_button.rect.collidepoint(pos):
                    if os.path.isfile("custom_field.txt"):
                        with open("custom_field.txt", "r") as f:
                            data = f.read()
                            data = data.split(",")
                            if len(data) >= 4:
                                messagebox.showerror("HEY!", "Hey!\n\nYou probably made an error in custom_field.txt. Make sure it's like '16,16,9' - without text, and only 3 numbers.\n\nThanks")
                            else:
                                try:
                                    options_and_cust = {
                                        "height": int(data[0]),
                                        "width": int(data[1]),
                                        "mines": int(data[2])
                                    }
                                    optionList.append(Options(int(data[1]), int(data[0]), int(data[2]))) 
                                    buttons(4)
                                except ValueError:
                                    messagebox.showinfo("HEY!", "Hey!\n\nYou forgot to enter something in custom_field.txt!")
                    else:
                        messagebox.showwarning('Custom field warning','Custom field is experimental feature - it can break the game\n\nIf you still want to use it, game will create .txt file called "custom_field.txt".\n\nAll you need to do - write info about your field, for e.g.\n\n "16,16,99" will generate 16x16 field with 99 mines.')
                        with open("custom_field.txt", "w") as f:
                            f.write(" ")
                            f.close()
            else:
                pass
        if not easy_button.alive() or not medium_button.alive() or not hard_button.alive() or not custom_button.alive():
            flag_txt = font1.render(f"{current_flag_num}/{max_flag_num}", 1, (255,255,255))
            window.blit(flag_txt, (385, 24))
            if not finish:
                global timer
                timer = font1.render(f"{minutes:02d}:{int(sec%60):02d}", 1, (255,255,255))
            window.blit(timer, (758, 24))
            gui_icons.draw(window)
        if not finish:
            pos = mouse.get_pos()
            if pos[0] < ((1200 - (fieldWidth * 32))/2) or pos[0] >= ((1200 - (fieldWidth * 32))/2) + fieldWidth*32:
                pass
            elif pos[1] < ((700 - (fieldHeight * 32))/2) or pos[1] >= ((700 - (fieldHeight * 32))/2) + fieldHeight*32:
                pass
            else:
                if event1.type == MOUSEMOTION:
                    hovered_sprites = [s for s in blocksList if s.rect.collidepoint(pos)]
                    hover()
                if event1.type == MOUSEBUTTONDOWN and event1.button == LEFT:
                    clicked_sprites = [s for s in blocksList if s.rect.collidepoint(pos)]
                    openblock()
                if event1.type == MOUSEBUTTONDOWN and event1.button == RIGHT:
                    clicked_sprites2 = [s for s in blocksList if s.rect.collidepoint(pos)]
                    flag()

        display.update()

    


start(3)

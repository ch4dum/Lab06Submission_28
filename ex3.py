import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(150,0,255),(self.x,self.y,self.w,self.h))
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    def isMouseOn(self):
        mx,my = pg.mouse.get_pos()
        if mx >= self.x and mx <= self.x+self.w:
            if my >= self.y and my <= self.y+self.h:
                pg.draw.rect(screen,(255,150,100),(self.x,self.y,self.w,self.h))
                if pg.mouse.get_pressed() == (1,0,0):
                    pg.draw.rect(screen,(255,245,100),(self.x,self.y,self.w,self.h))
                    return True
            else:
                pg.draw.rect(screen,(100,50,25),(self.x,self.y,self.w,self.h))
        else:
            pg.draw.rect(screen,(100,50,25),(self.x,self.y,self.w,self.h)) #ไม่กดแดง



pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color(100,50,25) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(255,150,100)     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(400, 100, 440, 32) # สร้าง InputBox2
input_box3 = InputBox(100, 200, 140, 32)
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('First Name', True, (255,150,100), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (120, 66)

text2 = font.render('Last Name', True, (255,150,100), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (420, 66)

text3 = font.render('Age', True, (255,150,100), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (66, 166)

btn = Button(400,200,160,32)
btn.isMouseOn()

text4 = font.render('SUBMIT', True, (255,250,255)) # (text,is smooth?,letter color,background color)
textRect4 = text4.get_rect() # text size
textRect4.center = (480, 216)

# text5 = font.render("Hello" + input_box1.text + input_box2.text + "!!! You are " + input_box3.text + " years old.", True, (255,150,100), (0,0,0)) # (text,is smooth?,letter color,background color)
# textRect5 = text5.get_rect() # text size
# textRect5.center = (400, 300)

while run:
    screen.fill((255, 255, 255))
    font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize

    text5 = font.render('',True,(255,150,100)) # (text,is smooth?,letter color,background color)
    textRect5 = text5.get_rect() # text size
    textRect5.center = (200, 300)
    if btn.isMouseOn() == True:
        text5 = font.render("Hello " + input_box1.text+ " " + input_box2.text + "!!! You are " + input_box3.text + " years old.", True, (255,150,100))
    else :
        text5 = font.render('',True,(255,150,100))
        
    
    
    # btn.draw(screen)
    # btn.isMouseOn
    btn.isMouseOn()
    screen.blit(text5, textRect5)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    #
    # pg.time.delay(1)
    pg.display.update()

    
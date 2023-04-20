import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    def isMouseOn(self):
        mx,my = pg.mouse.get_pos()
        if mx >= self.x and mx <= self.x+self.w:
            if my >= self.y and my <= self.y+self.h:
                pg.draw.rect(screen,(0,255,0),(self.x,self.y,self.w,self.h))
                if pg.mouse.get_pressed() == (1,0,0):
                    pg.draw.rect(screen,(0,0,255),(self.x,self.y,self.w,self.h))
            else:
                pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))
        else:
            pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h)) #ไม่กดแดง


pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,200,100) # สร้าง Object จากคลาส Button ขึ้นมา
squre = Rectangle(200,200,50,50)
btn.isMouseOn

while(run):
    screen.fill((255, 255, 255))
    btn.isMouseOn
    btn.isMouseOn()
    squre.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
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

pg.init()
run = True
win_x, win_y = 800, 600
screen = pg.display.set_mode((win_x, win_y))
squre = Rectangle(200,200,100,100)


while(run):
    screen.fill((255, 255, 255))
    squre.draw(screen)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            squre.x += 100
            print("Key D down")
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            squre.x -=100
            print("Key A down")
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            squre.y -=100
            print("Key W down")
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            squre.y +=100
            print("Key S down") 
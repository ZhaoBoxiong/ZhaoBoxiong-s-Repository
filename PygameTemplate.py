import pygame
from pygame.locals import *
from sys import exit

Screen_Witch = 800
Screnn_Height = 1000
ticks = 0

pygame.init()
Screen = pygame.display.set_mode([Screen_Witch,Screnn_Height])
pygame.display.set_caption("This is my test Program")
background = pygame.image.load("/Users/zhaoboxiong/PycharmProjects/Hash/bground.jpeg")
LuffyImg = pygame.image.load("/Users/zhaoboxiong/PycharmProjects/Hash/Plane.jpeg")

hero1_rect = pygame.Rect(101, 100, 363, 377)
hero1 = LuffyImg.subsurface(hero1_rect)

hero_pos = [0, 100]
hero_pos_T = [200, 300]
while True:
    Screen.blit(background,(0,0))

    if ticks % 50 > 25:
        Screen.blit(hero1, hero_pos)

    ticks += 1
    hero_pos = [hero_pos[0]+1,hero_pos[1]+1]
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



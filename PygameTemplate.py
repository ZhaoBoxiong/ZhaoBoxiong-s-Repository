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
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}
while True:
    Screen.blit(background,(0,0))

    Screen.blit(hero1, hero_pos)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = 3
        elif event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0


    offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
    hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]


#python 2.7
#classic breakout game, move the paddle to bounce the ball and clear rows of bricks
import pygame, sys
from time import sleep

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('Breakout')

screen.fill((255,255,255))

#paddle
paddle = pygame.draw.rect(screen, (139,0,0), (140,490,100,10))

#ball
ball = pygame.draw.circle(screen, (0,0,0), (190,482), 8)
pygame.display.update()

#main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()

#pygame.display.quit()
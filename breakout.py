#python 2.7
#classic breakout game, move the paddle to bounce the ball and clear rows of bricks
import pygame, sys
from time import sleep

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('Breakout')
pygame.key.set_repeat(50,50)

fps = pygame.time.Clock()

screen.fill((255,255,255))

#paddle
paddle_rect = pygame.Rect(140, 490, 100, 10)
paddle = pygame.draw.rect(screen, (139,0,0), paddle_rect)

#ball
ball_coord = [190, 482]
ball = pygame.draw.circle(screen, (0,0,0), ball_coord, 8)
pygame.display.update()

direction = ''

#main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      
    #get the direction of the key pressed
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        direction = 'RIGHT'
      elif event.key == pygame.K_LEFT:
        direction = 'LEFT'
      else:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
    #update position
    #(left, top, width, height)
  if direction == 'RIGHT':
    if paddle_rect.right + 10 <= 400:
      paddle_rect = paddle_rect.move(10, 0)
    else:
      pass
      #bounce it off and go left now?
  if direction == 'LEFT':
    if paddle_rect.left -10 < 0:
      paddle_rect = paddle_rect.move(-10, 0)
    else:
      pass
      #bounce it off and go right now?
  #direction = ''
    
    #paddle_coord = [140, 490, 100, 10]
  
  screen.fill((255,255,255))
  paddle = pygame.draw.rect(screen, (139, 0, 0), paddle_rect)
  ball = pygame.draw.circle(screen, (0,0,0), ball_coord, 8)
  
  pygame.display.update()
  
  
  fps.tick(20)

#pygame.display.quit()
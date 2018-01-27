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
paddle_rect = pygame.Rect(150, 490, 75, 10)
paddle = pygame.draw.rect(screen, (139,0,0), paddle_rect)

#ball
ball_coord = [190, 484]
ball = pygame.draw.circle(screen, (0,0,0), ball_coord, 7)

#bricks
bricks = []
for i in range(20, 110, 20):
  for j in range(0, 400, 50):
    bricks.append((j, i))
  
print bricks

colors = [(244, 69, 66), (235, 244, 66), (66, 244, 75), (66, 244, 22), (176, 66, 244)]

for b in bricks:
  c = (b[1]/20)-1
  pygame.draw.rect(screen, colors[c], pygame.Rect(b, (100, 20)))

direction = ''
pygame.display.update()

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
        
  #update position of paddle
  x = '' 
  if direction == 'RIGHT':
    if paddle_rect.right + 10 <= 400:
      paddle_rect = paddle_rect.move(10, 0)
    else:
      paddle_rect = paddle_rect.move(-10, 0)
      x = 'LEFT'
      
  if direction == 'LEFT':
    if paddle_rect.left - 10 >= 0:
      paddle_rect = paddle_rect.move(-10, 0)
    else:
      paddle_rect = paddle_rect.move(10, 0)
      x = 'RIGHT'

  if x == 'RIGHT':
    direction = x
  if x == 'LEFT':
    direction = x
    
  #ball graphics
  
  screen.fill((255,255,255))
  paddle = pygame.draw.rect(screen, (139, 0, 0), paddle_rect)
  ball = pygame.draw.circle(screen, (0,0,0), ball_coord, 7)
  for b in bricks:
    c = (b[1]/20)-1
    pygame.draw.rect(screen, colors[c], pygame.Rect(b, (100, 20)))
  
  pygame.display.update()
  
  
  fps.tick(20)

pygame.display.quit()
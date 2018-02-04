#python 2.7
#classic breakout game, move the paddle to bounce the ball and clear rows of bricks
import pygame, sys
from time import sleep

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('Breakout')
pygame.key.set_repeat(50,50)

fps = pygame.time.Clock()

screen.fill((32, 32, 32))

#paddle
paddle_rect = pygame.Rect(150, 490, 75, 10)
paddle = pygame.draw.rect(screen, (255, 0, 127), paddle_rect)

#ball
ball_coord = [188, 482]
vel = [3, 3]
ball = pygame.draw.circle(screen, (255, 255, 255), ball_coord, 8)

#bricks
bricks = []
for i in range(20, 110, 20):
  for j in range(0, 400, 50):
    bricks.append((j, i))

colors = [(255, 0, 0), (255, 255,  51), (51, 255, 51), (51, 255, 255), (178, 102, 255)]

bricks2 = []
for b in bricks:
  #c = (b[1]/20)-1
  rec = pygame.Rect(b, (100, 20))
  bricks2.append(rec)

for b in bricks2:
  c = (b[1]/20)-1
  pygame.draw.rect(screen, colors[c], b)

direction = ''
#currX = 150
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
      #currX += 10
    else:
      paddle_rect = paddle_rect.move(-10, 0)
      #currX -= 10
      x = 'LEFT'
      
  if direction == 'LEFT':
    if paddle_rect.left - 10 >= 0:
      paddle_rect = paddle_rect.move(-10, 0)
      #currX -= 10
    else:
      paddle_rect = paddle_rect.move(10, 0)
      #currX += 10
      x = 'RIGHT'

  if x == 'RIGHT':
    direction = x
  if x == 'LEFT':
    direction = x
  
  remove = []
  #brick boundaries
  for b in bricks2:
    if ball.colliderect(b):
      if ball_coord[0]-8 == b.bottom:
        vel[0] = -(vel[0])
        remove.append(b)
      elif ball_coord[0]+8 == b.top:
        vel[0] = -(vel[0])
        remove.append(b)
      elif ball_coord[1]-8 == b.right:
        vel[1] = -(vel[1])
        remove.append(b)
      else:
        vel[1] = -(vel[1])
        remove.append(b)
        
  #screen boundaries
  if ball_coord[0] + 8 >= 400:
    vel[0] = -(vel[0])
  if ball_coord[0] - 8 <= 0:
    vel[0] = -(vel[0])
  if ball_coord[1] - 8 <= 0:
    vel[1] = -(vel[1])
  
  #ball hits paddle
  if ball_coord[1] + 8 == 490 and ball_coord[0] - 8 >= paddle_rect.topleft[0] and ball_coord[0] + 8 <= paddle_rect.topright[0]:
    vel[1] = -(vel[1])
  
  ball_coord[0] = ball_coord[0] + vel[0]
  ball_coord[1] = ball_coord[1] + vel[1]
  
  #reset ball and paddle if the ball goes off screen
  if ball_coord[1] + 8 >= 500:
    paddle_rect = pygame.Rect(150, 490, 75, 10)
    ball_coord = [188, 482]
    vel = [3, 3]
  
  #redraw graphics
  screen.fill((32, 32, 32))
  paddle = pygame.draw.rect(screen, (255, 0, 127), paddle_rect)
  ball = pygame.draw.circle(screen, (255, 255, 255), ball_coord, 8)
  
  for r in remove:
    bricks2.remove(r)
  
  for b in bricks2:
    c = (b[1]/20)-1
    pygame.draw.rect(screen, colors[c], b)
  
  pygame.display.update()
  
  
  fps.tick(20)

pygame.display.quit()

#python 2.7
#classic breakout game, move the paddle to bounce the ball and clear rows of bricks
import pygame, sys, time

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('Breakout')
pygame.key.set_repeat(50,50)
gameScore = 0
lives = 3

fps = pygame.time.Clock()

screen.fill((32, 32, 32))

#paddle set up
paddle_rect = pygame.Rect(150, 490, 75, 10)
paddle = pygame.draw.rect(screen, (255, 0, 127), paddle_rect)

#ball set up
ball_coord = [188, 482]
vel = [4, 4]
ball = pygame.draw.circle(screen, (255, 255, 255), ball_coord, 8)

#brick set up
bricks = []
for i in range(20, 110, 20):
  for j in range(0, 400, 50):
    bricks.append((j, i))

colors = [(255, 0, 0), (255, 255,  51), (51, 255, 51), (51, 255, 255), (178, 102, 255)]

bricks2 = []
for b in bricks:
  rec = pygame.Rect(b, (50, 20))
  bricks2.append(rec)

for b in bricks2:
  c = (b[1]/20)-1
  pygame.draw.rect(screen, colors[c], b)

direction = ''
pygame.display.update()

#helper methods
def check_bounds(ball_coord, vel):
  if ball_coord[0] + 8 >= 400:
    vel[0] = -(vel[0])
  if ball_coord[0] - 8 <= 0:
    vel[0] = -(vel[0])
  if ball_coord[1] - 8 <= 0:
    vel[1] = -(vel[1])
    
  return vel

def move_paddle(direction, paddle_rect):
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
    
  return direction, paddle_rect

def move_ball(ball_coord, paddle_rect, vel):
  #if ball hits paddle
  if ball_coord[1] + 8 == 490 and ball_coord[0] - 8 >= paddle_rect.topleft[0] and ball_coord[0] + 8 <= paddle_rect.topright[0]:
    vel[1] = -(vel[1])
  
  #update ball coordinates
  ball_coord[0] = ball_coord[0] + vel[0]
  ball_coord[1] = ball_coord[1] + vel[1]
  
  return ball_coord, vel

def check_bricks(ball, ball_coord, bricks2, gameScore):
  remove = []
  for b in bricks2:
    if ball.colliderect(b):
      #account for score
      if b.top == 20:
        gameScore += 5
      elif b.top == 40:
        gameScore += 10
      elif b.top == 60:
        gameScore += 15
      elif b.top == 80:
        gameScore += 20
      else:
        gameScore += 25
      #change ball velocity
      if ball_coord[0] - 8 == b.bottom:
        vel[0] = -(vel[0])
        remove.append(b)
      elif ball_coord[0] + 8 == b.top:
        vel[0] = -(vel[0])
        remove.append(b)
      elif ball_coord[1] - 8 == b.right:
        vel[1] = -(vel[1])
        remove.append(b)
      else:
        vel[1] = -(vel[1])
        remove.append(b)
        
  return remove, vel, gameScore

def resetBall(ball_coord, lives):
  paddle_rect = pygame.Rect(150, 490, 75, 10)
  ball_coord = [188, 482]
  vel = [3, 3]
  lives -= 1
  return paddle_rect, ball_coord, vel, lives

#also handles displaying lives
def score():
  scoreFont = pygame.font.SysFont('comicsansms', 16)
  scoreScreen = scoreFont.render('Score: {0}'.format(gameScore), True, pygame.Color(255, 255, 255))
  livesScreen = scoreFont.render('Lives: {0}'.format(lives), True, pygame.Color(255, 255, 255))
  scoreRect = scoreScreen.get_rect()
  livesRect = livesScreen.get_rect()
  scoreRect.midtop = (35, 2)
  livesRect.midtop = (355, 2)
  screen.blit(scoreScreen, scoreRect)
  screen.blit(livesScreen, livesRect)
  
def gameOver():
  font = pygame.font.SysFont('comicsansms', 20)
  lines = 'Game Over. Your score: {0}'.format(gameScore)
  gameOverScreen = font.render(lines, True, pygame.Color(255, 255 , 255))
  gameOverRect = gameOverScreen.get_rect()
  gameOverRect.midtop = (200, 200)
  screen.blit(gameOverScreen, gameOverRect)
  pygame.display.flip()
  time.sleep(10)
  pygame.quit()
  sys.exit()
  
  
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
        
  #paddle movement
  direction, paddle_rect = move_paddle(direction, paddle_rect)
  
  #check what the ball hits
  remove, vel, gameScore = check_bricks(ball, ball_coord, bricks2, gameScore)
  vel = check_bounds(ball_coord, vel)
  ball_coord, vel = move_ball(ball_coord, paddle_rect, vel)
  
  #reset ball and paddle if the ball goes off screen
  if ball_coord[1] + 8 >= 500:
    paddle_rect, ball_coord, vel, lives = resetBall(ball_coord, lives)
    
  if lives == 0:
    gameOver()
  
  #redraw graphics
  screen.fill((32, 32, 32))
  paddle = pygame.draw.rect(screen, (255, 0, 127), paddle_rect)
  ball = pygame.draw.circle(screen, (255, 255, 255), ball_coord, 8)
  
  #account for change in bricks
  for r in remove:
    bricks2.remove(r)
  
  if len(bricks) == 0:
    gameOver()
    
  for b in bricks2:
    c = (b[1]/20)-1
    pygame.draw.rect(screen, colors[c], b)
  
  score()
  pygame.display.update()
  
  
  fps.tick(20)

pygame.display.quit()

#python 2.7
#2048 game
import pygame, time, sys

#initialization
pygame.init()

#screen
screen = pygame.display.set_mode((405, 470))
pygame.display.set_caption('2048')
screen.fill((255, 255, 255))

playRect = pygame.Rect(10, 75, 385, 385)
playSurface = pygame.draw.rect(screen, (0, 0, 0), playRect)

fps = pygame.time.Clock()
pygame.display.update()

values = [2, 4]

direction = ''
gameScore = 0
squares = []
"""
for x in range(15, 390, 95):
  for y in range(80, 390, 95):
    sq = pygame.Rect((x, y), (90, 90))
    squares.append(sq)
"""

squares.append(pygame.Rect((15, 80), (90, 90)))

for s in squares:
  pygame.draw.rect(screen, (0, 0, 255), s)

def movement(direction, squares):
  if direction == 'RIGHT':
    for i in range(len(squares)):
      #check bounds
      squares[i] = squares[i].move(40, 0)
  if direction == 'LEFT':
    for i in range(len(squares)):
      squares[i] = squares[i].move(-40, 0)
  if direction == 'UP':
    for i in range(len(squares)):
      squares[i] = squares[i].move(0, -35)
  if direction == 'DOWN':
    for i in range(len(squares)):
      squares[i] = squares[i].move(0, 35)
  return squares
  
def score():
  scoreFont = pygame.font.SysFont('comicsansms', 24)
  scoreScreen = scoreFont.render('Score: {0}'.format(gameScore), True, pygame.Color(0, 0, 0))
  scoreRect = scoreScreen.get_rect()
  scoreRect.midtop = (60,20)
  screen.blit(scoreScreen, scoreRect)
    
def gameOver():
  font = pygame.font.SysFont('comicsansms', 20)
  gameOverScreen = font.render('Game Over.', True, pygame.Color(0, 0, 0))
  gameOverRect = gameOverScreen.get_rect()
  gameOverRect.midtop = (250, 300)
  screen.blit(gameOverScreen, gameOverRect)
  pygame.display.flip()
  time.sleep(2)
  pygame.quit()
  sys.exit()
    
#game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    direction = ''
    #get key direction
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        direction = 'RIGHT'
      elif event.key == pygame.K_LEFT:
        direction = 'LEFT'
      elif event.key == pygame.K_DOWN:
        direction = 'DOWN'
      elif event.key == pygame.K_UP:
        direction = 'UP'
      else:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
  
  #square movement
  squares = movement(direction, squares)
  
  #redraw graphics
  screen.fill((255, 255, 255))
  playSurface = pygame.draw.rect(screen, (0, 0, 0), playRect)
  for s in squares:
    pygame.draw.rect(screen, (0, 0, 255), s)
  
  score()
  pygame.display.update()
  
  fps.tick(20)
  
pygame.display.quit()
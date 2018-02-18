import pygame,sys

pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Pong')

fps = pygame.time.Clock()

screen.fill((0, 0, 0))

def move_paddle():
  pass

def check_bounds():
  pass

def move_ball():
  pass

def reset_ball():
  pass

def set_score():
  pass

def game_over():
  pass

#direction holders for each player
directionOne = ''
directionTwo = ''

#main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    #key direction
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        directionOne = 'UP'
      if event.key == pygame.K_DOWN:
        directionOne = 'DOWN'
      if event.key == pygame.K_w:
        directionTwo = 'UP'
      if event.key == pygame.K_s:
        directionTwo = 'DOWN'
      if event.key == pygame.K_ESCAPE:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    print directionOne
    print directionTwo
    
    screen = pygame.display.set_mode((700, 400))
    screen.fill((0, 0, 0))
    
  fps.tick(20)
  pygame.display.update()
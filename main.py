import pygame
from constants import *
from player import Player
def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pyGameClock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  player = Player(x, y)
  while True:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
       for item in updatable:
            player.update(dt)
       screen.fill((0,0,0))
       for item in drawable:
            player.draw(screen)
       
       pygame.display.flip()
       dt = (pyGameClock.tick(60))/1000
       
       
if __name__ == "__main__":
	main()

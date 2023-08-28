import pygame as p
from typing import List

def main():
    # Run-of-the-mill pygame boilerplate
    p.init()
    display = p.display.set_mode((1280, 270))
    clock = pygame.time.clock()
    run = True

    # Enter game loop
    game_loop(run)


def game_loop(run: bool) -> int:
    pass


if __name__ == '__main__':
    main()
import traceback
import pygame as p
from typing import List
from _logging import Log
from datetime import datetime

def main():
    try:
        # Run-of-the-mill pygame boilerplate
        logfile = f"./logs/{datetime.now()}".replace(':', '-')
        log = Log(logfile, True)
        log.write_event(f"Succesfully opened logfile at {logfile}")
        log.write_event(f"Initializing pygame variables at {datetime.now()}")
        p.init()
        display = p.display.set_mode((1280, 270))
        clock = p.time.Clock()
        run = True

        # Enter game loop
        log.write_event(f"Entering game loop at {datetime.now()}")
        exit = game_loop(run, log)
        log.write_event(f"Shutting down with exit code {exit} at {datetime.now()}")
    except Exception as instance:
        log.write_fatal(f"Caught exception at {datetime.now()}")
        log.write_exception(f"{traceback.format_exc()}")

def game_loop(run: bool, log: Log) -> int:
    return 0


if __name__ == '__main__':
    main()
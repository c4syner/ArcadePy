from io_handler import IOHandler
from engine import TetrisEngine
import time

def main():
    terminal = IOHandler(50, 5)
    game = TetrisEngine(20, 20)
    board = game.getMap()
    for x, row in enumerate(board):
        for y, pointer in enumerate(row):
            terminal.writeCharToLocation(x, y, pointer, 2)
    terminal.refresh()
    
    terminal.getKey()
    terminal.revert()
if(__name__ == "__main__"):
    main()
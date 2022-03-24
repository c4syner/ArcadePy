import curses
import time

class IOHandler:
    def __init__(self, directCoordinateOffsetX: int = 0, directCoordinateOffsetY: int = 0) -> None:
        self.directCoordinateOffsetX = directCoordinateOffsetX
        self.directCoordinateOffsetY = directCoordinateOffsetY
        # Create a terminal object
        self.term = curses.initscr()
        self._initColorMap()
        self._unbufferedInput()

        self.MAX_X, self.MAX_Y = self.term.getmaxyx()
        

    def writeNewline(self, buffer, color_index: int = 1) -> None:
        # Write to a buffer with a specified color + newline "print()"
        self.term.addstr(f"{buffer}\n", curses.color_pair(color_index))
        self.refresh()

    def write(self, buffer, color_index: int = 1) -> None:
        # Write to a buffer with a specified color, "print()"
        self.term.addstr(buffer, curses.color_pair(color_index))
        self.refresh()

    def read(self, prompt: str = None) -> str:
        # Get input akin to input()
        self._bufferedInput()
        self.write(prompt if prompt else "")
        _input: str = self.term.getstr().decode()
        self._unbufferedInput()
        return _input
    
    def writeCharToLocation(self, x, y, char, color_index: int = 1) -> None:
        # Add char to the buffer
        self.term.addch(self.directCoordinateOffsetY + y, self.directCoordinateOffsetX + x, char, curses.color_pair(color_index))

    def clear(self) -> None:
        self._clear()

    def refresh(self) -> None:
        self._update()

    def revert(self) -> None:
        self._bufferedInput()
        curses.endwin()

    def getKey(self) -> str:
        return self._getch()
 
    def _initColorMap(self) -> None:
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    def _unbufferedInput(self) -> None:
        # Unbuffered input
        curses.cbreak()
        # No echo input
        curses.noecho()
    
    def _bufferedInput(self) -> None:
        # Echo input
        curses.echo()
        # Buffered input
        curses.nocbreak()

    def _getch(self) -> None:
        # Get character from keyboard
        return self.term.getkey()

    def _update(self) -> None:
        # Write screen buffer
        self.term.refresh()

    def _clear(self) -> None:
        # Clear terminal
        self.term.clear()
    


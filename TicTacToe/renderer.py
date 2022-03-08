from typing import *
import platform
import os

class Renderer:
    def __init__(self) -> None:
        self.charMap = {
            0: " ",
            1: "X",
            2: "O"
        }
    
        self.platformClearMap = {
            "Linux": "clear",
            "Darwin": "clear",
            "Windows": "cls"
        }
    
        self.P_COMMAND = self.platformClearMap[platform.system()]

    def _clear(self):
        os.system(self.P_COMMAND)
        
    def renderGameBoard(self, _array: List[List[int]]) -> None:
        for i, x in enumerate(_array):
            print("║", end =" ")
            for j, y in enumerate(x):
                boxChar  = "║"
                if(i == 1):
                    boxChar = "╬"
                print(self.charMap[y], boxChar, end = " ")
            print()


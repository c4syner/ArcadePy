from ast import Return
import random
import os
import subprocess

class Minesweeper:
    def __init__(self) -> None:
        self.LENGTH = 10
        self.DROP_RATE = .95

        self.gameBoard = self._generateGameBoard()
        self.workingGameBoard = self._generateEmptyGameBoard()
        self.charMap = {
            0: " ",
            1: "X",
            2: "⚑",
            3: "█"
        }
    
    def _clear(self):
        os.system("cls")

    def _generateCell(self):
        return 1 if random.random() > self.DROP_RATE else 0
    
    def _generateGameBoard(self):
        return [[self._generateCell() for a in range(self.LENGTH)] for x in range(self.LENGTH)]
    
    def _generateEmptyGameBoard(self):
        return [[0 for a in range(self.LENGTH)] for x in range(self.LENGTH)]

    def _render(self):
        self._clear()
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[0])):
                print(self.charMap[self.gameBoard[i][j]], end="")
            print()

    def beginGame(self):
        self._render()

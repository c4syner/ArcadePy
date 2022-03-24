from copy import deepcopy

CharacterMap = {
    0: "█",
}

class TetrisEngine:
    def __init__(self, width: int = 20, height: int = 50) -> None:
        self.width = width
        self.height = height
        self.DEFAULT = self._loadEmptyBoard()
        self.map = deepcopy(self.DEFAULT)
        
    def getMap(self) -> list[list[str]]:
        return self.map

    def _loadEmptyBoard(self) -> None:
        _map: list = []
        for x in range(self.width):
            _row = []
            for y in range(self.height):
                _row.append(0)
            _map.append(_row)
        return _map
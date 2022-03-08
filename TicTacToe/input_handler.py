
class InputHandler:
    def __init__(self) -> None:
        pass
    def _validateInput(self, board, x,y):
        try:   
            if(board[x][y] != 0):
                return False
            return True
        except:
            return False
    
    def getInput(self, board):
        X_Coord = int(input("Pick an X coordiante "))
        Y_Coord = int(input("Pick a Y coordinate "))
        if(not self._validateInput(board, X_Coord, Y_Coord)):
            self.getInput(board)
        return (X_Coord, Y_Coord)



            
           
           





            

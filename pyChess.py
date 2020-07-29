class piece():
    def __init__(self, team, piece, startSquare):
        self.team = team
            #"black" or "white"
        self.piece = piece
            #K-King Q-Queen X-Bishop #-Rook H-Horse P-Pawn
        self.currentSpace = startSquare
        self.firstTurn = True
        
        #Sets piece color
        if self.team == "white":
            self.icon = f"\033[1;30;47m {piece} \033[1;37;49m"
        elif self.team == "black":
            self.icon = f"\033[1;37;44m {piece} \033[1;37;49m"
        else:
            print("Invalid team")
        
    #updates piece and changes firstTurn for pawns, and castling.
    def movePiece(self, newSpace):
        self.currentSpace = newSpace
        self.firstTurn = False
        
    def validMove(self, newSpace):
        #For direction, zero is towards higher values, 
        
        #ord turns letters into numbers. - 96 is not normalize it to a=1
        currentSpace = [ord(self.currentSpace[0]) - 96, int(self.currentSpace[1])]
        validMoves = []
        
        #Checks piece type, then adds all theoretically possible moves on a chessboard 8 spaces away in every direction.
        #Best if used in with isOnBoard()
        
        if self.piece == "K":
            validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] + 1}")
            validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] - 1}")
            validMoves.append(f"{letterDict[currentSpace[0] + 1 ]}{currentSpace[1]}")
            validMoves.append(f"{letterDict[currentSpace[0] - 1 ]}{currentSpace[1]}")
                                                                     
            validMoves.append(f"{letterDict[currentSpace[0] + 1 ]}{currentSpace[1] + 1}")
            validMoves.append(f"{letterDict[currentSpace[0] + 1 ]}{currentSpace[1] - 1}")
            validMoves.append(f"{letterDict[currentSpace[0] - 1 ]}{currentSpace[1] + 1}")
            validMoves.append(f"{letterDict[currentSpace[0] - 1 ]}{currentSpace[1] - 1}")
                    
        
        elif self.piece == "Q":
            for x in range(8):
                x += 1
                validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] + x}")
                validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] - x}")
                validMoves.append(f"{letterDict[currentSpace[0] + x]}{currentSpace[1]}")
                validMoves.append(f"{letterDict[currentSpace[0] - x]}{currentSpace[1]}")
                                                                        
                validMoves.append(f"{letterDict[currentSpace[0] + x]}{currentSpace[1] + x}")
                validMoves.append(f"{letterDict[currentSpace[0] + x]}{currentSpace[1] - x}")
                validMoves.append(f"{letterDict[currentSpace[0] - x]}{currentSpace[1] + x}")
                validMoves.append(f"{letterDict[currentSpace[0] - x]}{currentSpace[1] - x}")
        
        elif self.piece == "X":
            for x in range(8):
                x += 1                                                                        
                validMoves.append(f"{letterDict[currentSpace[0] + x]}{currentSpace[1] + x}")
                validMoves.append(f"{letterDict[currentSpace[0] + x]}{currentSpace[1] - x}")
                validMoves.append(f"{letterDict[currentSpace[0] - x]}{currentSpace[1] + x}")
                validMoves.append(f"{letterDict[currentSpace[0] - x]}{currentSpace[1] - x}")
        
        elif self.piece == "#":
            for x in range(8):
                x += 1
                validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] + x}")
                validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] - x}")
                validMoves.append(f"{letterDict[currentSpace[0] + x]}{currentSpace[1]}")
                validMoves.append(f"{letterDict[currentSpace[0] - x]}{currentSpace[1]}")
        
        elif self.piece == "H":
            validMoves.append(f"{letterDict[currentSpace[0] + 2]}{currentSpace[1] + 1}")
            validMoves.append(f"{letterDict[currentSpace[0] + 2]}{currentSpace[1] - 1}")
            validMoves.append(f"{letterDict[currentSpace[0] - 2]}{currentSpace[1] + 1}")
            validMoves.append(f"{letterDict[currentSpace[0] - 2]}{currentSpace[1] - 1}")
            validMoves.append(f"{letterDict[currentSpace[0] + 1]}{currentSpace[1] + 2}")
            validMoves.append(f"{letterDict[currentSpace[0] - 1]}{currentSpace[1] + 2}")
            validMoves.append(f"{letterDict[currentSpace[0] + 1]}{currentSpace[1] - 2}")
            validMoves.append(f"{letterDict[currentSpace[0] - 1]}{currentSpace[1] - 2}")
        
        elif self.piece == "P":
            if self.team == "white":
                validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] + 1}")
                
                if self.firstTurn:
                    validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] + 2}")
            
            elif self.team == "black":
                validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] - 1}")
                
                if self.firstTurn:
                    validMoves.append(f"{letterDict[currentSpace[0]]}{currentSpace[1] - 2}")
            
        if newSpace in validMoves:
            return True
        else:
            return False
        
        

boardDict = {

    "a1": " ",
    "b1": " ",
    "c1": " ",
    "d1": " ",
    
    "e1": " ",
    "f1": " ",
    "g1": " ",
    "h1": " ",
    
    "a2": " ",
    "b2": " ",
    "c2": " ",
    "d2": " ",
    
    "e2": " ",
    "f2": " ",
    "g2": " ",
    "h2": " ",
    
    "a3": " ",
    "b3": " ",
    "c3": " ",
    "d3": " ",
    
    "e3": " ",
    "f3": " ",
    "g3": " ",
    "h3": " ",
    
    "a4": " ",
    "b4": " ",
    "c4": " ",
    "d4": " ",
    
    "e4": " ",
    "f4": " ",
    "g4": " ",
    "h4": " ",
    
    "a5": " ",
    "b5": " ",
    "c5": " ",
    "d5": " ",
    
    "e5": " ",
    "f5": " ",
    "g5": " ",
    "h5": " ",
    
    "a6": " ",
    "b6": " ",
    "c6": " ",
    "d6": " ",
    
    "e6": " ",
    "f6": " ",
    "g6": " ",
    "h6": " ",
    
    "a7": " ",
    "b7": " ",
    "c7": " ",
    "d7": " ",
    
    "e7": " ",
    "f7": " ",
    "g7": " ",
    "h7": " ",
    
    "a8": " ",
    "b8": " ",
    "c8": " ",
    "d8": " ",
    
    "e8": " ",
    "f8": " ",
    "g8": " ",
    "h8": " ",

}


pieceDict = {
    
    #Create all the piece objects
    
    "pawnW1"  : piece("white", "P", "a2"),
    "pawnW2"  : piece("white", "P", "b2"),
    "pawnW3"  : piece("white", "P", "c2"),
    "pawnW4"  : piece("white", "P", "d2"),
              
    "pawnW5"  : piece("white", "P", "e2"),
    "pawnW6"  : piece("white", "P", "f2"),
    "pawnW7"  : piece("white", "P", "g2"),
    "pawnW8"  : piece("white", "P", "h2"),
    
    "rookW1"  : piece("white", "#", "a1"),
    "rookW2"  : piece("white", "#", "h1"),
    
    "knightW1": piece("white", "H", "b1"),
    "knightW2": piece("white", "H", "g1"),
    
    "bishopW1": piece("white", "X", "c1"),
    "bishopW2": piece("white", "X", "f1"),
    
    "kingW"   : piece("white", "K", "e1"),
    
    "queenW"  : piece("white", "Q", "d1"),
    
    
    
    "pawnB1"  : piece("black", "P", "a7"),
    "pawnB2"  : piece("black", "P", "b7"),
    "pawnB3"  : piece("black", "P", "c7"),
    "pawnB4"  : piece("black", "P", "d7"),
              
    "pawnB5"  : piece("black", "P", "e7"),
    "pawnB6"  : piece("black", "P", "f7"),
    "pawnB7"  : piece("black", "P", "g7"),
    "pawnB8"  : piece("black", "P", "h7"),
    
    "rookB1"  : piece("black", "#", "a8"),
    "rookB2"  : piece("black", "#", "h8"),
    
    "knightB1": piece("black", "H", "b8"),
    "knightB2": piece("black", "H", "g8"),
    
    "bishopB1": piece("black", "X", "c8"),
    "bishopB2": piece("black", "X", "f8"),
    
    "kingB"   : piece("black", "K", "e8"),
    
    "queenB"  : piece("black", "Q", "d8"),

}


letterDict = {
    
    -8: "x",
    -7: "x",
    -6: "x",
    -5: "x",
    -4: "x",
    -3: "x",
    -2: "x",
    -1: "x",
    0: "x",
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "x",
    10: "x",
    11: "x",
    12: "x",
    13: "x",
    14: "x",
    15: "x",
    16: "x",

}

def printBoard(boardDict):
    line = "---"
    blankLine = "{:^3}|{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}|".format(" ",line, line, line, line, line, line, line, line)
    
    time.sleep(1)
    
    for x in range(20):
        print("\n")
    
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("8", boardDict["a8"], boardDict["b8"], boardDict["c8"], boardDict["d8"], boardDict["e8"], boardDict["f8"], boardDict["g8"], boardDict["h8"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("7", boardDict["a7"], boardDict["b7"], boardDict["c7"], boardDict["d7"], boardDict["e7"], boardDict["f7"], boardDict["g7"], boardDict["h7"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("6", boardDict["a6"], boardDict["b6"], boardDict["c6"], boardDict["d6"], boardDict["e6"], boardDict["f6"], boardDict["g6"], boardDict["h6"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("5", boardDict["a5"], boardDict["b5"], boardDict["c5"], boardDict["d5"], boardDict["e5"], boardDict["f5"], boardDict["g5"], boardDict["h5"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("4", boardDict["a4"], boardDict["b4"], boardDict["c4"], boardDict["d4"], boardDict["e4"], boardDict["f4"], boardDict["g4"], boardDict["h4"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("3", boardDict["a3"], boardDict["b3"], boardDict["c3"], boardDict["d3"], boardDict["e3"], boardDict["f3"], boardDict["g3"], boardDict["h3"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("2", boardDict["a2"], boardDict["b2"], boardDict["c2"], boardDict["d2"], boardDict["e2"], boardDict["f2"], boardDict["g2"], boardDict["h2"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format("1", boardDict["a1"], boardDict["b1"], boardDict["c1"], boardDict["d1"], boardDict["e1"], boardDict["f1"], boardDict["g1"], boardDict["h1"]))
    print(blankLine)
    print("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format(" ","a","b","c","d","e","f","g","h"))
    
    
def gameSetup(boardDict, pieceDict):
    #Grabbing all icons for pieces and placing them in their initial positions
    for x in pieceDict:
        boardDict[pieceDict[x].currentSpace] = pieceDict[x].icon
        
#Updates the board dictionary, call BEFORE switching turn~~!
def updateBoard(selectedPiece, selectedMove, pieceDict, boardDict):
    oldMove = selectedPiece.currentSpace
    boardDict[oldMove] = " "
    boardDict[selectedMove] = selectedPiece.icon
    
    #Handles deleting 
    for x in pieceDict:
        if pieceDict[x].currentSpace == selectedPiece.currentSpace and pieceDict[x] != selectedPiece:
            del pieceDict[x]
            break
            
    
    
#Run at the end of turn, after moves have been made. Call AFTER Update Board~~!
def switchTurn(currentTurn):
    if currentTurn == "white":
        return "black"
    elif currentTurn == "black":
        return "white"

#Checks if a space is on the board. Call during moving and selection.
def isOnBoard(space):
    x = space[0]
    y = int(space[1])
    
    x = ord(x) - 96

    if x > 8 or x < 1 or y > 8 or y < 1:
        return False
    else:
        return True

    
def SpaceToPiece(pieceDict, selectedSpace):
    #Reset variable to pass through if statement if a viable piece is not found
    pieceIndex = None
            
    #Setup to grab selectedPieceIndex
    for x in pieceDict:
                
        #iterate through pieceDict, grabbing the current space of each piece
        testSpace = pieceDict[x].currentSpace
                
        #Test if the space of the piece matches the space selected
        if testSpace == selectedSpace:
                    
            #if a matching value is found, catch selectedPieceIndex and close loop
            PieceIndex = x
            break
            
    return selectedPieceIndex

#UNFINISHED
def isInCheck(pieceDict, team):
    if team == "white":
        pieceIndex = "kingW"
    elif team == "black":
        pieceIndex = "kingB"
        
    possibleAttacksArray = []
    currentSpace = pieceDict[pieceIndex].currentSpace

    return False

#UNFINISHED
def collisionCheck():
    pass


if __name__ == "__main__":
    import time
    turn = "white"
    gameRunning = True
    
    #Initializes board for first time, initializes all piece objects
    gameSetup(boardDict, pieceDict)
    
    #LOGIC REWRITE
    while gameRunning == True:
        #Run check for king in check at the beginning of every turn. Players should have warning!
        
        #Print board 
        printBoard(boardDict)
        
        #Print info
        print("\n")
        print(f"Turn: {turn}")
        
        #Wait for piece select input
        #Waits for piece select input
        selectedPiece = input("Select piece to move: ")
        
        #Check if there is a piece on that space
        selectedPieceIndex = SpaceToPiece(pieceDict, selectedPiece)

            
        #Eliminate and pass if selectedPieceIndex is not caught
        if selectedPieceIndex == None:
            print("Please select a space with one of your pieces.")
        
        elif pieceDict[selectedPieceIndex].team == turn:
            #Continue Game Logic
            
            #Wait for move selection input
            selectedMove = input("Select space to move to: ")
            
            #Check if move is on the board
            #Check if move is valid
            
            if isOnBoard(selectedMove) and pieceDict[selectedPieceIndex].validMove(selectedMove):
                
            #Check if the king is in check in current configuration
            #Check if the king is in check in the theoretical configuration
            #Check if there is already a piece there, remove it if opposite team and cancel if same team
            #Check if pawn reached the last line of the board, if yes then promote. Promote func in piece class.
            
                #Run the update board function to ... update the board. Passes in the particular piece that moves.
                updateBoard(pieceDict[selectedPieceIndex], selectedMove, pieceDict, boardDict)
                        
                #Update the piece object's position
                pieceDict[selectedPieceIndex].movePiece(selectedMove)
                        
                #Switch the turn!
                turn = switchTurn(turn)
            
            
        else:
            #Reset
            print("Please select a valid piece!")
        
        

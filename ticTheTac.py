import random

def drawBoard(board):
    # Draws the board based on the board list.
    print('1      |2      |3')
    print('       |       |')
    print('   ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3])
    print('_______|_______|_______')
    print('4      |5      |6')
    print('       |       |')
    print('   ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6])
    print('_______|_______|_______')
    print('7      |8      |9')
    print('       |       |')
    print('   ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9])
    print('       |       |       ')

def getSymbols():
    # Asks the player to define their symbol and the computer's, makes sure they are 1 character long and different.
    playerSymbol = ''
    computerSymbol = ''
    print('What symbol do you want to use?')
    while (len(playerSymbol) != 1) or (playerSymbol == ' '):
        playerSymbol = input()
        if (len(playerSymbol) != 1) or (playerSymbol == ' '):
            print('Symbols must be 1 character long. What symbol do you want to use?')
    print('What symbol do you want the computer to use?')
    while (len(computerSymbol) != 1) or (playerSymbol == ' ') or (computerSymbol == playerSymbol):
        computerSymbol = input()
        if (len(computerSymbol) != 1) or (computerSymbol == ' '):
            print('Symbols must be 1 character long. What symbol do you want to the computer use?')
        if computerSymbol == playerSymbol:
            print('The computer needs a different symbol. What symbol do you want to the computer use?')
    # Returns the player and computer symbols.
    return playerSymbol, computerSymbol

def whoGoes():
    # Randomly chooses who goes first.
    decision = random.randint(0,1)
    if decision == 0:
        return 'player'
    else:
        return 'computer'

def checkEmpty(board, move):
    # Checks if a space is empty
    return board[int(move)] == '_'

def checkWin(board, symbol):
    return ((board[1] == board[2] == board[3] == symbol) or # Checks the top.
    (board[4] == board[5] == board[6] == symbol) or # Check horizontal middle.
    (board[7] == board[8] == board[9] == symbol) or # Checks the bottom.
    (board[1] == board[4] == board[7] == symbol) or # Checks the left side.
    (board[2] == board[5] == board[8] == symbol) or # Checks vertical middle.
    (board[3] == board[6] == board[9] == symbol) or # Checks right side.
    (board[1] == board[5] == board[9] == symbol) or # Checks diagonal left.
    (board[3] == board[5] == board[7] == symbol)) # Checks diagonal right.

def checkTie(board):
    # Checks if every space has been used, returns False if there are empty spaces.
    for i in range(1,10):
        if checkEmpty(board, i):
            return False
    else:
        return True


def playerMove(board, playerSymbol):
    # Gets the player's move, check to make sure it is valid, then returns it.
    move = '_'
    while (move not in '1 2 3 4 5 6 7 8 9'.split()) or (not checkEmpty(board,int(move))):
        print('Where do you want to go?')
        move = input()
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('That\'s not a valid move.')
        elif not checkEmpty(board,int(move)):
            print('Choose an empty space.')
    return int(move)

def makeMove(board, symbol, move):
    board[move] = symbol

def resetBoard(board):
    # Resets the board, and prepares it for a new game.
    for i in range(len(board)):
        board[i] = '_'

def copyBoard(board):
    # Makes a copy of the board, and returns it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def computerMove(board, playerSymbol, computerSymbol):
    moveOptions = []
    # Checks for wins on next move, chooses randomly amongst them.
    for i in range(1,10):
        if checkEmpty(board, i):
            copy = copyBoard(board)
            copy[i] = computerSymbol
            if checkWin(copy, computerSymbol):
                moveOptions.append(i)
    if len(moveOptions) >= 1:
        choice = random.randint(0,len(moveOptions)-1)
        return moveOptions[choice]
    # Checks for player wins on next move, chooses randomly amongst them.
    for i in range(1,10):
        if checkEmpty(board, i):
            copy = copyBoard(board)
            copy[i] = playerSymbol
            if checkWin(copy, playerSymbol):
                moveOptions.append(i)
    if len(moveOptions) >= 1:
        return random.choice(moveOptions)
    # Checks for available corners, chooses randomly amongst them.
    for i in [1,3,7,9]:
        if checkEmpty(board, i):
            moveOptions.append(i)
    if len(moveOptions) >= 1:
        return random.choice(moveOptions)
    # Takes the center, if available.
    if checkEmpty(board, 5):
        return 5
    # Randomly takes a remaining square.
    else:
        for i in [2,4,6,8]:
            if checkEmpty(board, i):
                moveOptions.append(i)
    if len(moveOptions) >= 1:
        return random.choice(moveOptions)

def playAgain():
    # Returns True if the player wants to play again, and false otherwise.
    print('Do you want to play again? (yes / no)')
    playAgain = input().lower()
    if playAgain.startswith('y'):
        return True
    else:
        return False
            
def playGame():
    play = True
    print('[ T I C   T A C   T O E ]')
    while play:
        board = ['_'] * 10
        print()
        playerSymbol, computerSymbol = getSymbols()
        turn = whoGoes()
        print()
        if turn == 'player':
            drawBoard(board)
            print()
            print('You go first!')
        elif turn == 'computer':
            print('The computer goes first!')
        while True:
            if turn == 'player':
                print()
                makeMove(board, playerSymbol, playerMove(board, playerSymbol))
                if checkWin(board, playerSymbol):
                    print()
                    drawBoard(board)
                    print()
                    print('You win!')
                    print()
                    play = playAgain()
                    break
                elif checkTie(board):
                    print()
                    drawBoard(board)
                    print()
                    print('Cat\'s game.')
                    print()
                    play = playAgain()
                    break
                else:
                    turn = 'computer'
            elif turn == 'computer':
                makeMove(board, computerSymbol, computerMove(board, playerSymbol, computerSymbol))
                print()
                drawBoard(board)
                if checkWin(board, computerSymbol):
                    print()
                    print('The computer wins!')
                    print()
                    play = playAgain()
                    break
                elif checkTie(board):
                    print()
                    print('Cat\'s game.')
                    print()
                    play = playAgain()
                    break
                else:
                    turn = 'player'
    print('Sorry to hear that. Play again soon!')


playGame()

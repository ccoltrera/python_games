import random
import sys

def showInstructions():
    # Displays instructions, if a player wants to see them.
    print('Welcome to MINESWEEPER! Do you want to see instructions? (yes / no)')
    answer = ''
    while not answer.lower().startswith('y') and not answer.lower().startswith('y'):
        answer = input()
        if answer.lower().startswith('n'):
            print()
            return
        elif answer.lower().startswith('y'):
            break
        else:
            print('You must answer yes or no.')
    print('''
Someone has scattered mines all over the ground! Isolate the mines by
revealing all of the clear areas, but be careful not to reveal a mine.

When a clear spot is revealed, you can see the number of adjacent mines.
Blank spots mean there are no adjacent mines.


ex:

        1  1  2  1  1
        
  1  1  2  M  2  M  1
  
  1  M  3  2  3  1  1
  
  1  1  2  M  1
  
        1  1  1


If a revealed spot is clear, all clear spaces it shares a side with will
also be revealed.
''')
    print('Press \'enter\' to continue.')
    input()
    print('''- CHECK spots for mines, type x and y coordinates separated by a space.

ex: 2 3

- FLAG spots which you think have mines, type 'f' and x and y
coordinates, separated by spaces. There are as many flags as mines.

ex: f 2 3

- UNFLAG spots by typing 'f' and x and y coordinates, separated by spaces.

ex: u 2 3

- QUIT the game by typing 'quit'.

ex: quit

That's all there is to it. Good luck with your sweeping!
''')

def genNewBoard(width, height):
    # Generates a blank board data structure, with a specified width and height.
    newBoard = []
    for i in range(width):
        newBoard.append([])
        for y in range(height):
            newBoard[i].append('-')
    return newBoard

def getRow(board,rowNum):
    row = []
    for i in range(len(board)):
        row.append(board[i][rowNum])
    return row

def drawBoard(board, mineList, numFlags):
    print()
    print('Mines: ' + str(len(mineList)))
    print('Remaining flags: ' + str(numFlags))
    print()
    # If needed, prints enough tens-place x-coordinates for the size of the board.
    if len(board) > 10:
        print('   ', end='')
        for i in range(len(board)):
            if i == len(board) - 1:
                if int(i/10) == 0:
                    print('   ')
                else:
                    print(' ' + str(int(i/10)) + ' ')
            else:
                if int(i/10) == 0:
                    print('   ', end='')
                else:
                    print(' ' + str(int(i/10)) + ' ', end='')
    # Prints enough ones-place x-coordinates for the size of the board.
    print('   ', end='')
    for i in range(len(board)):
        if i == len(board) - 1:
            if len(str(i)) <= 1:
                print(' ' + str(i) + ' ')
            else:
                print(' ' + str(i)[1] + ' ')
        else:
            if len(str(i)) <= 1:
                print(' ' + str(i) + ' ', end='')
            else:
                print(' ' + str(i)[1] + ' ', end='')
    # Prints enough dashes to top the box around the board.
    print('   ', end='')
    for i in range(len(board)):
        if i < len(board) - 1:
            print('———', end='')
        else:
            print('———')
    # Prints y-coordinates, followed vertical lines and rows.
    for i in range(len(board[0])):
        ySpaces = 2 - len(str(i))
        print(' ' * ySpaces + str(i) + '|', end='')
        print(' ' + '  '.join(getRow(board,i)) + ' |', end='')
        print(str(i))
        # Prints blank rows with vertical lines between each row.
        if i < len(board[0]) - 1:
            print('  |' + '   ' * len(board) + '|')
    # Prints enough dashes to complete the outline box around the board.
    print('   ', end='')
    for i in range(len(board)):
        if i < len(board) - 1:
            print('———', end='')
        else:
            print('———')
    # If needed, prints enough tens-place x-coordinates along the bottom of the board.
    if len(board) > 10:
        print('   ', end='')
        for i in range(len(board)):
            if i == len(board) - 1:
                if int(i/10) == 0:
                    print('   ')
                else:
                    print(' ' + str(int(i/10)) + ' ')
            else:
                if int(i/10) == 0:
                    print('   ', end='')
                else:
                    print(' ' + str(int(i/10)) + ' ', end='')
    # Prints enough ones-place x-coordinates along the bottom of the board.
    print('   ', end='')
    for i in range(len(board)):
        if i == len(board) - 1:
            if len(str(i)) <= 1:
                print(' ' + str(i) + ' ')
            else:
                print(' ' + str(i)[1] + ' ')
        else:
            if len(str(i)) <= 1:
                print(' ' + str(i) + ' ', end='')
            else:
                print(' ' + str(i)[1] + ' ', end='')
    print()
    
def placeMines(board,numMines):
    # Randomly generates a list of mines.
    mineList = []
    while len(mineList) < numMines:
        mineX = random.randint(0,len(board)-1)
        mineY = random.randint(0,len(board[0])-1)
        if [mineX, mineY] not in mineList:
            mineList.append([mineX, mineY])
    return mineList

def adjMines(mineList, x, y):
    # Returns the number of mines adjacent to a given x, y coordinate.
    numMines = 0
    # Checks the square above-left, if there is one.
    if y != 0 and x != 0:
        if [x - 1, y - 1] in mineList:
            numMines += 1
    # Checks the square above, if there is one.
    if y != 0:
        if [x, y - 1] in mineList:
            numMines += 1
    # Checks the square above-right, if there is one.
    if y != 0:
        if [x + 1, y - 1] in mineList:
            numMines += 1
    # Checks the square to the right.
    if [x + 1, y] in mineList:
        numMines += 1
    # Checks the square below-right.
    if [x + 1, y + 1] in mineList:
        numMines += 1
    # Checks the square below.
    if [x, y + 1] in mineList:
        numMines += 1
    # Checks the square below-left, if there is one.
    if x != 0:
        if [x - 1, y + 1] in mineList:
            numMines += 1
    # Checks the square to the left, if there is one.
    if x != 0:
        if [x - 1, y] in mineList:
            numMines += 1
    return numMines

def revealSquare(mineList, x, y):
    # Returns the identity of an individual square.
    if [x, y] in mineList:
        return 'M'
    elif adjMines(mineList, x, y) > 0:
        return '%s' % str(adjMines(mineList, x, y))
    else:
        return ' '

def revealBoard(board, mineList):
    # Edits the board to reveal mines, adjacents, and clears.
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y] = revealSquare(mineList, x, y)

def checkWin(board, mineList):
    # Checks if every non-mine square has been revealed, returns True if they have.
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != revealSquare(mineList, x, y) and revealSquare(mineList, x, y) != 'M':
                return False
    return True

def flagSquare(board, x, y):
    # Flags a square on the board.
    board[x][y] = '/'

def removeFlag(board, x, y):
    # Removes a flag from a square.
    board[x][y] = '-'

def chooseSquare(board, mineList, x, y):
    # Reveals a given square and all adjacent non-mine / non-flagged squares.
    toCheck = [[x,y]]
    checked = []
    while len(toCheck) > 0:
        coord = toCheck[0]
        checked.append(coord)
        coordIdent = revealSquare(mineList, coord[0], coord[1])
        # Checks if a square is a mine, in which case adjacent squares are not checked.
        if coordIdent != 'M':
            # Adds upper adjacent square to toCheck if it exists and not in checked.
            if coord[1] != 0 and [coord[0], coord[1] - 1] not in checked:
                toCheck.append([coord[0], coord[1] - 1])
            # Adds right adjacent square to toCheck if on the board not in checked
            if coord[0] < len(board) - 1 and [coord[0] + 1, coord[1]] not in checked:
                toCheck.append([coord[0] + 1, coord[1]])
            # Adds lower adjacent square to toCheck if on the board and not in checked.
            if coord[1] < len(board[coord[0]]) - 1 and [coord[0], coord[1] + 1] not in checked:
                toCheck.append([coord[0], coord[1] + 1])
            # Adds left adjacent square to toCheck if it exists and not in checked.
            if coord[0] != 0 and [coord[0] - 1, coord[1]] not in checked:
                toCheck.append([coord[0] - 1, coord[1]])
        # Reveals a square if neither flagged nor a mine.
        if board[coord[0]][coord[1]] != '/' and coordIdent != 'M':
            board[coord[0]][coord[1]] = coordIdent
        toCheck.remove(coord)

def getBoardSize(minWidth, maxWidth, minHeight, maxHeight):
    # Returns a list with the width and height of the board the player wants, within the specified perameters.
    # First, generates lists of possible strings for width and height.
    widthRange = list(range(minWidth, maxWidth + 1))
    for i in range(len(widthRange)):
        widthRange[i] = str(widthRange[i])
    heightRange = list(range(minHeight, maxHeight + 1))
    for i in range(len(heightRange)):
        heightRange[i] = str(heightRange[i])
    # Asks for a width, makes sure it is an allowed value.
    print('Choose the width of your board, between %s and %s (inclusive): ' % (str(minWidth), str(maxWidth)), end='')
    boardWidth = ''
    while boardWidth not in widthRange:
        boardWidth = input()
        if boardWidth not in widthRange:
            print('Width must be a numeral between %s and %s (inclusive): ' % (str(minWidth), str(maxWidth)), end='')
    # Asks for a height, makes sure it is an allowed value.
    print('Choose the height of your board, between %s and %s (inclusive): ' % (str(minHeight), str(maxHeight)), end='')
    boardHeight = ''
    while boardHeight not in heightRange:
        boardHeight = input()
        if boardHeight not in heightRange:
            print('Width must be a numeral between %s and %s (inclusive): ' % (str(minWidth), str(maxWidth)), end='')
    # Returns a list with integers for width and height.
    return int(boardWidth), int(boardHeight)

def playAgain():
    # Returns True if the player wants to play again, else returns False
    print('Do you want to play again? (yes / no)')
    return input().lower().startswith('y')

def onBoard(board, xString, yString):
    # Checks if given strings can be integers within the range of the board.
    try:
        x = int(xString)
        y = int(yString)
        if x > len(board) - 1:
            return False
        elif y > len(board[0]) - 1:
            return False
        else:
            return True
    except ValueError:
        return False

def isOpen(board, x, y):
    try:
        return board[int(x)][int(y)] == '-'
    except ValueError:
        return False
    

def validMove(board, moveInput, numFlags):
    # Checks if an input actually corresponds to an available square on the board.
    move = moveInput.split()
    # Check if the length of the input is too long.
    if len(move) > 3 or len(move) < 2:
        return False
    # Check if the provided x and y values can be integers within the range of the board.
    elif len(move) == 2:
        if onBoard(board, move[0],move[1]):
            return isOpen(board, move[0],move[1])
        else:
            return False
    # Check if a move is a flag place or flag remove, and check if it's valid.
    elif len(move) == 3:
        if move[0].lower() == 'f':
            # Checks if there are flags remaining, otherwise returns False.
            if numFlags == 0:
                return False
            else:
                if onBoard(board, move[1], move[2]):
                    return isOpen(board, move[1],move[2])
        elif move[0].lower() == 'u':
            # Checks if there are flags on the board.
            if onBoard(board, move[1], move[2]):
                    return board[int(move[1])][int(move[2])] == '/'
            else:
                return False
        else:
            return False
    else:
        return False

def chooseDiff():
    # Returns a multiplier for the numMines
    print('Choose a difficulty level (easy, medium, hard): ', end='')
    diff = ''
    while not diff.lower().startswith('e') and not diff.lower().startswith('m') and not diff.lower().startswith('h'):
        diff = input()
        if not diff.lower().startswith('e') and not diff.lower().startswith('m') and not diff.lower().startswith('h'):
            print('You must choose easy, medium, or hard: ', end='')
    if diff.lower().startswith('e'):
        return 0.16
    elif diff.lower().startswith('m'):
        return 0.25
    elif diff.lower().startswith('h'):
        return 0.33

        
def playGame():
    playing = True
    while playing:
        print('M I N E   S W E E P E R')
        print()
        # Gives optional instructions
        showInstructions()
        # Gets board size, and generates a board.
        boardSize = getBoardSize(5,15,5,10)
        board = genNewBoard(boardSize[0], boardSize[1])
        # Generates a number of mines based on the difficulty and the number squares.
        mineMult = chooseDiff()
        numMines = int((boardSize[0] * boardSize[1]) * mineMult)
        mineList = placeMines(board, numMines)
        numFlags = len(mineList)
        moveNum = 1
        while not checkWin(board, mineList):
            drawBoard(board, mineList, numFlags)
            # Gets a move from the player, and checks that it's valid. Displays flag option if flags left, unflag if flags on board.
            print('CHECK (x y)', end='')
            if numFlags > 0 and moveNum > 1:
                print(' / FLAG (f x y)', end='')
            if numFlags < numMines:
                print(' / UNFLAG (u x y)', end='')
            print(' / QUIT (quit): ', end='')
            moveInput = ''
            while not validMove(board, moveInput, numFlags):
                moveInput = input()
                if moveInput.lower() == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                if not validMove(board, moveInput, numFlags):
                    print('Sorry, that\'s not a valid move.')
                    print('CHECK (x y)', end='')
                    if numFlags > 0 and moveNum > 1:
                        print(' / FLAG (f x y)', end='')
                    if numFlags < numMines:
                        print(' / UNFLAG (u x y)', end='')
                    print(' / QUIT (quit): ', end='')
            move = moveInput.split()
            # If move is a flag plant, plants a flag
            if move[0].lower() == 'f':
                flagSquare(board,int(move[1]),int(move[2]))
                numFlags -= 1
            # If move is a flag removal, removes a flag
            elif move[0].lower() == 'u':
                removeFlag(board,int(move[1]),int(move[2]))
                numFlags += 1
            else:
                if moveNum == 1:
                    # If the first move finds a mine, changes the mine list. 
                    while revealSquare(mineList,int(move[0]),int(move[1])) == 'M':
                        mineList = placeMines(board, numMines)
                    chooseSquare(board, mineList, int(move[0]), int(move[1]))
                    # If the first move wins, changes the mine list. 
                    while checkWin(board, mineList):
                        board = genNewBoard(boardSize[0], boardSize[1])
                        mineList = placeMines(board, numMines)
                        chooseSquare(board, mineList, int(move[0]), int(move[1]))
                    moveNum += 1
                # Checks if the move is a mine.
                elif moveNum > 1 and revealSquare(mineList,int(move[0]),int(move[1])) == 'M':
                    print()
                    print('You hit a bomb! You lose.')
                    revealBoard(board, mineList)
                    break
                # Chooses a square, and iterates the number of moves
                else:
                    chooseSquare(board, mineList, int(move[0]), int(move[1]))
                    moveNum += 1
            if checkWin(board, mineList):
                print()
                print('You\'ve isolated all the bombs! You win.')
        revealBoard(board, mineList)
        drawBoard(board, mineList, numFlags)
        playing = playAgain()
        print()
                
            


#revealBoard(board, mineList)

#chooseSquare(board, mineList, 10, 10)
playGame()

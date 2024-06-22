import random
import itertools

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board
def printBoard(board):
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

# take player input
def playerInput(board):
    for retry in itertools.count(start=1):
        inp = int(input("Enter a number 1 thru 9: "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break
        else:
            print(f"Invalid input")

#check if win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

#switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

# computer
def computer(board):
    while currentPlayer == "O" and winner == None:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        print(f"The winner is {winner}")
        checkWin.has_been_called = True
checkWin.has_been_called = False

def checkTie(board):
    global gameRunning
    if "-" not in board and checkWin.has_been_called == False:
        print("Its a tie")
        printBoard(board)
        gameRunning = False
        checkTie.has_been_called = True
checkTie.has_been_called = False

#choosing between player or computer
def chooseMode():
    inp = 0
    while inp != 1 or inp != 2:
        inp = int(input("Choose between playing against a player (1) or a computer (2): "))
        if inp == 1:
            while gameRunning == True:
                printBoard(board)
                if checkWin.has_been_called == True or checkTie.has_been_called == True:
                    break
                playerInput(board)
                checkWin()
                checkTie(board)
                switchPlayer()
            break
        elif inp == 2:
            while gameRunning == True:
                printBoard(board)
                if checkWin.has_been_called == True or checkTie.has_been_called == True:
                    break
                playerInput(board)
                checkWin()
                checkTie(board)
                switchPlayer()
                if checkWin.has_been_called == True or checkTie.has_been_called == True:
                    printBoard(board)
                    break
                computer(board)
                checkWin()
                checkTie(board)
                if checkWin.has_been_called == True or checkTie.has_been_called == True:
                    printBoard(board)
                    break
            break
        else:
            print("Invalid input, try again.")

# the game
chooseMode()
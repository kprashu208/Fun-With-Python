
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('    |    |   ')
    print('  ' + board[1] + ' | ' + board[2] + '  |  ' + board[3])
    print('    |    |   ')
    print('--------------')
    print('    |    |   ')
    print('  ' + board[4] + ' | ' + board[5] + '  |  ' + board[6])
    print('    |    |   ')
    print('--------------')
    print('    |    |   ')
    print('  ' + board[7] + ' | ' + board[8] + '  |  ' + board[9])
    print('    |    |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def IsWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))


def playerMove():
    run = True
    while run:
        moves = input("Please enter a position for 'X' between 1-9.")
        try:
            move = int(moves)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied.")
                    print("Choose any other number between 1-9.")
            else:
                print("Please enter a number bwtween 1-9 only.")
        except:
            print("Please enter a valid number")





def computerMove():
    possibleMoves = [ x for x, letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            tempBoard = board[:]
            tempBoard[i] = let

            if IsWinner(tempBoard, let):
                move = i
                return move

    if 5 in possibleMoves:
        move = 5
        return move

    cornersAvailable = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersAvailable.append(i)

    if len(cornersAvailable) > 0:
        move = selectRandom(cornersAvailable)
        return move

    edgesAvailable = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesAvailable.append(i)

    if len(edgesAvailable) > 0:
        move = selectRandom(edgesAvailable)
        return move

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the GAME")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board, 'O')):
            playerMove()
            if isBoardFull(board):
                printBoard(board)
        else:
            print("Sorry, you loose!!")
            break

        if not(IsWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O', move)
                printBoard(board)
                print("Computer place an O on the position", move ,":")
        else:
            print("YOU WIN")
            break

    if isBoardFull(board):
        print("Tie Game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() =='y':
        board = [' ' for x in range(10)]
        print('---------------------')
        main()
    else:
        break

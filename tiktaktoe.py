#global variables
global board
global turn
global emptyToken

#set up global tokens
emptyToken="_"
board=[[emptyToken for i in range(3)]for r in range(3)]
turn=0

# draw game board
def drawboard():
    print("#| 0 1 2")
    print("-+------")
    for i in range(3):
        print(str(i) +"|", end="")
        for c in range(3):
            print(board[c][i]+" ", end="")
        print()

#get current turn
def getTurn():
    if(turn%2==0):
        return "X"
    else:
        return "O"

# ask the user for coordinates for turn
def getcoords():
    print("Player " + getTurn()+ "'s turn.")
    isValid = True
    x=0
    y=0
    while(isValid):
        try:
            x=int(input("input x-coordinate:"))
            y=int(input("input y-coordinate:"))
            if(board[x][y]==emptyToken):
                isValid=False
            else:
                print("invalid entry, try again")
        except:
            print("invalid entry, try again")
    print()
    return x,y

    #check if game is done
def isFinished():
    # check rows
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and (board[i][0]!=emptyToken)):
            return 1
    #check col

        if(board[0][i]==board[1][i] and board[1][i]==board[2][i] and (board[0][i]!=emptyToken)):
            return 1
    #check diagnal
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and (board[0][0]!=emptyToken)):
        return 1
    elif(board[2][0]==board[1][1] and board[1][1]==board[0][2] and (board[2][0]!=emptyToken)):
        return 1

    #check for draw
    if(turn>=8):
        return 0
    #game isnt done
    return 2

#actual game
while(True):
    drawboard()
    x,y=getcoords()
    print("hi")
    board[x][y]=getTurn()
    state=isFinished()
    if(state==1 or state==0):
        break
    turn+=1

drawboard()
if(state==0):
    print("game ends in draw")
else:
    print(getTurn()+ " has won")

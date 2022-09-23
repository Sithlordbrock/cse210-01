# Assn Tic-Tac-Toe By: Brock Ford

def printBoard(grid):
    for i in grid:
        print()
        print("-+-+-")
        for j in i:
            print(f"{j}|", end="")
    print()

def playerMessage(currentPlayer, player1, player2):
    options = ["1","2","3","4","5","6","7","8","9"]
    selected = input(f"{currentPlayer}'s turn to choose a square (1-9): ")
    if selected in options:
        if selected in player1:
            print("The other player has chosen that, try again...")
            return playerMessage(currentPlayer,player1,player2)
        if selected in player2:
            print("The other player has chosen that, try again...")
            return playerMessage(currentPlayer,player1,player2)
        return selected
    else:
        print("That is not a vaid option try again...")
        return playerMessage(currentPlayer,player1,player2)


def checkForWin(player):
    winningCombo = [[1,4,7], [2,5,8], [3,6,9],
                [1,2,3], [4,5,6], [7,8,9],
                [1,5,9], [3,5,7]]
    result = False
    counter = 0
    for i in winningCombo:
        counter = 0
        for j in i:
            if str(j) in player:
                counter +=1
                if counter == 3:
                    result = True
    return result
            

    
def main():
    player1 = [""]
    player2 = [""]
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    player1Name = input("Welcome to Tic-Tac-Toe! What is player 1's name: ")
    player2Name = input("What is player 2's name: ")
    print(f"All righty then! Welcome {player1Name.capitalize()} and {player2Name.capitalize()}! {player1Name.capitalize()} will start the game!")
    keepPlaying = True
    currentPlayer = 1
    turnCounter = 0
    while (keepPlaying):
        printBoard(grid)
        #toggle which player is up
        if currentPlayer == 1:
            player1Choice = playerMessage(player1Name.capitalize(),player1,player2)
            player1.append(player1Choice)
            currentPlayer = 0
            if player1Choice == "1":
                grid[0][0] = "x"
            elif player1Choice == "2":
                grid[0][1] = "x"
            elif player1Choice == "3":
                grid[0][2] = "x"
            elif player1Choice == "4":
                grid[1][0] = "x"
            elif player1Choice == "5":
                grid[1][1] = "x"
            elif player1Choice == "6":
                grid[1][2] = "x"
            elif player1Choice == "7":
                grid[2][0] = "x"
            elif player1Choice == "8":
                grid[2][1] = "x"
            elif player1Choice == "9":
                grid[2][2] = "x"
            if checkForWin(player1):
                keepPlaying = False
                print(f"{player1Name.capitalize()} wins!")
        #if player 2's turn
        else: 
            player2Choice = playerMessage(player2Name.capitalize(),player1,player2)
            player2.append(player2Choice)
            currentPlayer = 1

            if player2Choice == "1":
                grid[0][0] = "o"
            elif player2Choice == "2":
                grid[0][1] = "o"
            elif player2Choice == "3":
                grid[0][2] = "o"
            elif player2Choice == "4":
                grid[1][0] = "o"
            elif player2Choice == "5":
                grid[1][1] = "o"
            elif player2Choice == "6":
                grid[1][2] = "o"
            elif player2Choice == "7":
                grid[2][0] = "o"
            elif player2Choice == "8":
                grid[2][1] = "o"
            elif player2Choice == "9":
                grid[2][2] = "o"

            if checkForWin(player2):
                keepPlaying = False
                print(f"{player2Name.capitalize()} wins!")
    
        turnCounter += 1
        if turnCounter > 8:
            keepPlaying = False

    printBoard(grid)
    if turnCounter > 8:
        print(f"It was a tie for {player1Name.capitalize()} and {player2Name.capitalize()}! Better luck next time!")
    print("Good Game! Thanks for playing!")




main()
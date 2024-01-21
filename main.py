from board import Game
from bot import Bot


def PlayOnePlayerGame(playerOneIcon, playerTwoIcon):
    didSomeoneWin = list([False, ""])

    comp = Bot(0)

    game = Game(playerOneIcon, playerTwoIcon, True)

    playerOnesTurn = True

    while True:
        game.PrintBoard()

        if playerOnesTurn:
            print("Players 1 Turn:")
        else:
            comp.DoMove(game)
            didSomeoneWin = game.CheckForWin()

            if didSomeoneWin[0]:
                game.PrintBoard()
                return didSomeoneWin
            if didSomeoneWin[1] == "draw":
                game.PrintBoard()
                return didSomeoneWin
            playerOnesTurn = not playerOnesTurn
            continue

        userInput = input()

        if userInput == "q":
            return didSomeoneWin

        try:
            userInput = int(userInput)
        except ValueError:
            print("Input a Number")
            continue

        game.DoMove(userInput, playerOnesTurn)

        game.PrintBoard()

        playerOnesTurn = not playerOnesTurn

        didSomeoneWin = game.CheckForWin()

        if didSomeoneWin[0]:
            return didSomeoneWin
        if didSomeoneWin[1] == "draw":
            return didSomeoneWin



def PlayTwoPlayerGame(playerOneIcon, playerTwoIcon):
    didSomeoneWin = list([False, ""])

    game = Game(playerOneIcon, playerTwoIcon, False)

    playerOnesTurn = True

    while True:
        game.PrintBoard()

        if playerOnesTurn:
            print("Players 1 Turn:")
        else:
            print("Players 2 Turn:")

        userInput = input()

        if userInput == "q":
            return didSomeoneWin

        try:
            userInput = int(userInput)
        except ValueError:
            print("Input a Number")
            continue

        game.DoMove(userInput, playerOnesTurn)

        game.PrintBoard()

        playerOnesTurn = not playerOnesTurn

        didSomeoneWin = game.CheckForWin()

        if didSomeoneWin[0]:
            return didSomeoneWin
        if didSomeoneWin[1] == "draw":
            return didSomeoneWin

def main():
    playerOneIcon = "X"
    playerTwoIcon = "O"

    while True:
        print("SinglePlayer(1) or MultiPlayer(2)")
        userInput = input()
        if userInput == "1":
            didSomeoneWin = PlayOnePlayerGame(playerOneIcon, playerTwoIcon)
            # print("SinglePlayer is Currently a WIP")
            # didSomeoneWin = [True, playerOneIcon]
            break
        elif userInput == "2":
            didSomeoneWin = PlayTwoPlayerGame(playerOneIcon, playerTwoIcon)
            break
        elif userInput == "q":
            return
        else:
            print("Enter Valid Input")



    if didSomeoneWin[0]:
        if didSomeoneWin[1] == playerOneIcon:
            print("Player 1 Wins")
        elif didSomeoneWin[1] == playerTwoIcon:
            print("Player 2 Wins")
    else:
        if didSomeoneWin[1] == "draw":
            print("Draw")
        else:
            print("Exited Game")


if __name__ == '__main__':
    main()
class Game:
    def __init__(self, playerOneIcon: str, playerTwoIcon: str, isSinglePlayer: bool):
        self.playerOneIcon = playerOneIcon
        self.playerTwoIcon = playerTwoIcon
        self.isSinglePlayer = isSinglePlayer
        self.board = [(f'{i}', False) for i in range(1, 10)]
    def PrintBoard(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.board[0][0], self.board[1][0], self.board[2][0]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.board[3][0], self.board[4][0], self.board[5][0]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.board[6][0], self.board[7][0], self.board[8][0]))
        print("\t     |     |")
        print("\n")

    def DoMove(self, position: int, playersOneTurn: bool):
        actualPosition = position - 1

        cell = list(self.board[actualPosition])

        if cell[1]:
            print("Already Taken")
            return
        else:
            cell[1] = True

        if playersOneTurn:
            icon = self.playerOneIcon
        else:
            icon = self.playerTwoIcon

        cell[0] = str(icon)

        cell = tuple(cell)

        self.board[actualPosition] = cell

    def CheckForWin(self):
        fullBoard = list(self.board)

        board = []

        for cell in fullBoard:
            board.append(cell[0])

        if board[0] == board[1] == board[2]:
            return [True, board[0]]
        elif board[3] == board[4] == board[5]:
            return [True, board[3]]
        elif board[6] == board[7] == board[8]:
            return [True, board[6]]
        elif board[0] == board[4] == board[8]:
            return [True, board[0]]
        elif board[2] == board[4] == board[6]:
            return [True, board[2]]
        elif board[0] == board[3] == board[6]:
            return [True, board[0]]
        elif board[1] == board[4] == board[7]:
            return [True, board[1]]
        elif board[2] == board[5] == board[8]:
            return [True, board[2]]

        filledCellCount = 0

        numberList = [f'{i}' for i in range(1, 10)]

        for cell in board:
            if cell not in numberList:
                filledCellCount += 1

        if filledCellCount == 9:
            return [False, "draw"]

        return [False, ""]



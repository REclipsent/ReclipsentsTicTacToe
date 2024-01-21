import random as rnd
from board import Game
class Bot:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def DoMove(self, currentGame: Game):
        botMove = None

        if self.difficulty == 0:
            while True:
                botMove = rnd.randint(1, 9)

                botMoveActual = botMove - 1

                if currentGame.board[botMoveActual][1]:
                    continue
                else:
                    break
        elif self.difficulty == 1:
            while True:
                if not currentGame.board[4][0]:
                    botMove = 5
                    break

                botMove = rnd.randint(1, 9)

                botMoveActual = botMove - 1

                if currentGame.board[botMoveActual][1]:
                    continue
                else:
                    break

        currentGame.DoMove(botMove, False)


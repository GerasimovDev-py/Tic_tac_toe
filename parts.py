class Board:
    def __init__(self):
        self.board = [['' for _ in range(5)] for _ in range(7)]


    def make_move(self, row, col,player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 4)
class Board:
    def __init__(self):
        self.field_size = 3 
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)  # Увеличил для лучшего отображения

    def check_win(self, player):
        # Проверка строк
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]):
                return True
        
        # Проверка столбцов
        for j in range(3):
            if all([self.board[i][j] == player for i in range(3)]):
                return True
        
        # Проверка диагоналей
        if all([self.board[i][i] == player for i in range(3)]):
            return True
        if all([self.board[i][2-i] == player for i in range(3)]):
            return True
        
        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True


from gameparts.exception import CellOccupiedError
from gameparts.exception import FieldIndexError

def main(): 
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    
    while running:
        print(f'Ход делает {current_player}')
        
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца зановo.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')2
                print('Введите другие координаты')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break
        
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        
        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'  # Исправлено: 'O' вместо '0'

if __name__ == '__main__':
    main()
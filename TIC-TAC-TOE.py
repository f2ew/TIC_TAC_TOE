class TicTacToe():

    def __init__(self):
        self.map = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.play_game()

    def play_game(self):
        self.draw()
        rounds = -1
        while not self.is_win():
            rounds += 1
            if rounds == 9:
                print('Ничья!')
                break
            self.set_cell(rounds)
            self.draw()


    def set_cell(self, rounds):
        if (rounds % 2) == 0:
            val = "X"
        else:
            val = "O"
        position = self.get_position(rounds, val)
        self.map[position] = val

    def get_position(self, rounds, val):
        while True:
            try:
                position = int(input(f"Введи номер клетки для {val}: "))
                self.is_set(position)
                return position
            except:
                print("Некорректный ввод. Попробуй ещё раз.")
                continue

    def is_set(self, position):
        if not isinstance(self.map[position], int):
            raise ValueError()
        else:
            return False

    def draw(self):
        for i in range(9):
            print(f'[{self.map[i]}]', end='')
            if (i + 1) % 3 == 0:
                print('')

    def is_win(self):
        win_list = ([0,1,2], [0, 4, 8], [0, 3, 6], [1,4,7], [2,4,6], [2,5,8], [3, 4, 5], [6,7,8])

        corr_list_X = [i for i in range(9) if self.map[i] == "X"]
        corr_list_O = [i for i in range(9) if self.map[i] == "O"]

        win = [True for i in range(8) if set(win_list[i]).issubset(corr_list_X) or set(win_list[i]).issubset(corr_list_O)]

        if any(win):
            print('Победа!')
            return True

        return False

if __name__ == '__main__':
    print("Запускаю крестики-нолики")
    TicTacToe()
    input()

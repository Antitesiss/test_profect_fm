import random

class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships = ships
        self.ships_alive = ships
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def display(self, show_ships=False):
        print("    A B C D E F G H I J")

        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is not None and show_ships:
                    display_row += "■ "
                else:
                    display_row += "O "

            line_number = i + 1
            if line_number != 10:
                print(line_number, " ", display_row)
            else:
                print(line_number, "", display_row)

class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15

        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def player_turn(self, x, y):
        lti = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

        if x not in lti:
            print("Ошибка!")
            return

        if not (1 <= y <= 10):
            print("Ошибка!")
            return

        x_coord = lti[x]
        y_coord = y - 1

        computer_grid = self.computer_field.grid

        if computer_grid[y_coord][x_coord] == "S":
            print("Вы попали!")
            computer_grid[y_coord][x_coord] = "X"
            self.computer_field.ships_alive -= 1
        else:
            print("Промах!")
            if computer_grid[y_coord][x_coord] != "X":
                computer_grid[y_coord][x_coord] = "O"

    def computer_turn(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            cell = self.player_field.grid[y][x]

            if cell not in ('X', 'O'):
                break

        if cell == 'S':
            print("Компьютер попал!")
            self.player_field.grid[y][x] = 'X'
            self.player_field.ships_alive -= 1
        else:
            print("Компьютер промахнулся!")
            self.player_field.grid[y][x] = 'O'

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display()

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
        self.player_field.display(show_ships=True)

        while True:
            while True:
                try:
                    x = input("Введите букву: ").upper()
                    if x not in 'ABCDEFGHIJ':
                        raise ValueError
                    y = int(input("Введите число: "))
                    if y < 1 or y > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Попробуйте снова.")

            self.player_turn(x, y)

            if self.computer_field.ships_alive <= 0:
                print("Вы победили! Все корабли компьютера потоплены!")
                return

            self.computer_turn()

            if self.player_field.ships_alive <= 0:
                print("Вы проиграли! Все ваши корабли потоплены!")
                return


game = BattleshipGame()
game.play()
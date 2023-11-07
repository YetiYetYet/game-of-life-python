import game_of_life


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    game_grid = game_of_life.GameGrid((10, 40))
    game_grid.init_grid_random()
    game_grid.print_grid()
    while True:
        user_input = input("Press a touch to continue or 'q' to quit: ")

        if user_input == 'q':
            break

        game_grid.print_grid()
        game_grid.update_next_generation()

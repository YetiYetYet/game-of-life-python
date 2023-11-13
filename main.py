from src import game_of_life


def init_game_of_life_module(custom_settings_input: bool = False):
    if custom_settings_input:
        size_x: int = int(input("Enter the size of the grid in x (default 40): ") or 40)
        size_y: int = int(input("Enter the size of the grid in y (default 10): ") or 10)
        life_spawn_probability: float = float(input("Enter the probability of life spawn (default 0.5) : ") or 0.5)

        game_grid = game_of_life.GameGrid((size_y, size_x))
        game_grid.init_grid_random(life_spawn_probability)
    else:
        game_grid = game_of_life.GameGrid((10, 40))
        game_grid.init_grid_random()

    while True:
        game_grid.print_grid_info()
        game_grid.print_grid()
        user_input = input("Press a touch to continue or 'q' to quit: ")

        if user_input == 'q':
            break

        game_grid.update_next_generation()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_game_of_life_module(custom_settings_input=True)

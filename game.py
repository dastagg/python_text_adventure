from player import Player


def play():
    """
    This is the main loop of the game.

    play loops through all the actions
    """
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        action_input = get_player_command()
        action_input = action_input.lower()
        if action_input == "n":
            print("Go North!")
        elif action_input == "s":
            print("Go South!")
        elif action_input == "e":
            print("Go East!")
        elif action_input == "w":
            print("Go West!")
        elif action_input == "i":
            player.print_inventory()
        else:
            print("Invalid action!")


def get_player_command():
    return input("Action: ")


play()

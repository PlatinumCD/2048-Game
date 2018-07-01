"""
Overall control for 2048 clone 512.  Coordinates
model and view and implements controller
functionality by interpreting keyboard input
"""
import model
import view
import keypress 


def main():
    # Set up model component
    grid = model.Grid()
    # Set up view component
    game_view = view.GameView(600, 600)
    grid_view = view.GridView(game_view, len(grid.tiles))
    grid.add_listener(grid_view)
    # Handle control component responsibility here
    commands = keypress.Command(game_view)
    grid.place_tile()

    # *** EXTRA CREDIT ***
    # The tile will not be placed if
    # a tile was not moved.

    grid.place_tile()
    gridlist = []
    gridlist.append(grid.as_list())

    # Game continues until there is no empty
    # space for a tile

    while grid.find_empty():

        if gridlist[-1] != grid.as_list(): # <------ EC
            grid.place_tile()              # <------ EC

        cmd = commands.next()
        if cmd == keypress.LEFT:
            gridlist.append(grid.as_list())
            grid.left()
        elif cmd == keypress.RIGHT:
            gridlist.append(grid.as_list())
            grid.right()
        elif cmd == keypress.UP:
            gridlist.append(grid.as_list())
            grid.up()
        elif cmd == keypress.DOWN:
            gridlist.append(grid.as_list())
            grid.down()
        else: 
            assert cmd == keypress.UNMAPPED

    game_view.lose(grid.score())


if __name__ == "__main__":
    main()

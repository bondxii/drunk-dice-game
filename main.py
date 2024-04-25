# Main window to start the game logic

from game.logic import Single_player
import game.drunkui as gui

def main():
    s_p = Single_player()
    s_p.roll_check()
    # gui.root.mainloop()

if __name__ == '__main__':
    main()
# Main window to start the game logic

from game.logic import Single_player

def main():
    s_p = Single_player()
    s_p.user_playing()

if __name__ == '__main__':
    main()
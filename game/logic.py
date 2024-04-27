# Here lies main logic of the game
# Maybe it shuld be deleted after changing structure for GUI to work
import random as r
# import game.logic as ui


# Main gaming scripts
def rolling() -> int:
        dice = r.randint(1, 6)
        return dice
    
def ai_rolling() -> int:
        dice = r.randint(2, 6)
        return dice    
                 
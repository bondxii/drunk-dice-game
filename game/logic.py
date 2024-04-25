# Here lies main logic of the game
# Maybe it shuld be deleted after changing structure for GUI to work

import random as r

class Single_player():
    
    # Main random method that generates nums 1-6    
    def rolling(self) -> int:
        dice = r.randint(1, 6)
        return dice
    
    # User decision to play or not
    def ask_to_play(self) -> bool:
        print('Whant to make new roll?')
        user_choice = input('[y/n]: ')
        match user_choice:
            case 'y':
                self.user_playing()
                return True
            case 'n':
                return
            case _:
                print('Invalid input')
                return self.ask_to_play()
    
    
    # Method that checks nums
    def user_playing(self) -> bool:
        num = self.rolling()
        print(num)
        if num == 1:
            print('You failed!')
            return True
        else:
            self.ask_to_play()       
        return False   
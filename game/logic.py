# Here lies main logic of the game
# Maybe it shuld be deleted after changing structure for GUI to work
import random as r

class Single_player():
    
    user_score = 0
    
    # Main random method that generates nums 1-6    
    def rolling(self) -> int:
        dice = r.randint(1, 6)
        return dice
    
    # User decision to play or not
    def ask_to_play(self) -> bool:
        tries = 3
        while tries > 0:
            res = self.rolling()
            print(res)
            if res == 1:
                return True
            else:
                print(f'You have {tries} tries.')
                print('Want to make new roll?')
                user_choice = input('[y/n]: ').lower()
                if user_choice == 'y':
                    tries -= 1
                elif user_choice == 'n':
                    self.user_score += res
                    print(f'Your score is {self.user_score}')
                    break
                else:
                    print('Wrong input!')
        return False
    
    
    
    
    def roll_check(self) -> None:
        game = True
        while game:
            result = self.ask_to_play()
            if result:
                print('Game over! Bye')
                game = False
            else:
                ai_score = r.randint(2, 6)
                if self.user_score > ai_score:
                    print(f'Ai: {ai_score} | You: {self.user_score}')
                    print('You won!')
                    game = False
                elif self.user_score < ai_score:
                    print(f'Ai: {ai_score} | You: {self.user_score}')
                    print('You lose...')
                    game = False
                else:
                    print(f'Ai: {ai_score} | You: {self.user_score}')
                    print('It\'s a match!')
                    game = False            
        
            
        
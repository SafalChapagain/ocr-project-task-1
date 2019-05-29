
"""SongSession class

Handles what happens every time a new song is being guessed by the player"""
class SongSession:
    lives = 2
    
    def __init__(self, song, game):
        self.song = song
        self.game = game

    """guess() -> bool guessedCorrectly

    Gets user input from the player to guess the song name"""
    def guess(self):
        while self.lives > 0: # Until the user runs out of lives
            guess = input("What is your guess?: ")

            if guess.lower() == self.song.name.lower(): # Check if they guessed correctly
                print("That is correct!")

                if self.lives == 2:
                    self.game.score += 3 # If the user only guessed once, add 3 points
                else:
                    self.game.score += 1 # If the user had to guess twice, add 1 point

                return True
            else:
                self.lives -= 1 # Take away a life
                print("Oh no, that's not the name of the song... You have {} {} left.".format(self.lives, "chances" if self.lives != 1 else "chance"))
				
        return False

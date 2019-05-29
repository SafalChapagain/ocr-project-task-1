import json
import random
from modules.songsession import SongSession
from modules.game import Game
from modules.song import Song

AUTHENTICATION_FILENAME = "resources/auth.json" # File which contains usernames and passwords


"""login(details) -> successful, username

Checks if login is correct
first return is if the login was successful,
second return is the username"""
def login(details):
    username = input("Enter your username: ")

    if username == "" or username not in auth: # Check if username is in auth file
        print("Username does not exist.")
        return False, None
    else:
        password = input("Enter your password: ")

        if password == auth[username]: # Check if password entered is the password of the user
            return True, username
        else:
            print("Incorrect password.")
            return False, None        
    


#Authentication
with open(AUTHENTICATION_FILENAME, "r") as authentication_file: # Open the authentication file
    auth = json.load(authentication_file)

success = False

while not success: # Try to login until correct username and password is entered
    success, username = login(auth)

print("Login successful. You are logged in as {}.".format(username))

game = Game(username) # Create instance of the Game class found in modules/game.py

succeeded = True
    
while succeeded: 
    succeeded = game.newSongSession(game.randomSong()) # Generate new song session

game.gameOver() # Game over as the player did not succeed

input("Press Enter to continue...")

import json
import random
from modules.song import Song
from modules.songsession import SongSession

MUSICLIST_FILENAME = "./resources/musiclist.json" # File which contains the songs and the artists
LEADERBOARD_FILENAME = "resources/leaderboard.json" # File which contains high scores

"""Game class

Handles the SongSessions and the main game. Keeps track of the users score."""
class Game:
    score = 0
    session = None
    
    def __init__(self, username):
        self.username = username
        self.chosenSongs = [] # List which stores the indexes of chosen songs in musiclist
        
        with open(MUSICLIST_FILENAME, "r") as musiclist_file:
            self.musiclist = [Song(x) for x in json.load(musiclist_file)] # Get the songs from the resources/musiclist.json file

    """Get a random song which hasn't been done before"""
    def randomSong(self):
        if len(self.chosenSongs) == len(self.musiclist): # Check if all of the songs have been gone through to reset the chosen song list
            print("You've gone through all of the songs!")
            self.chosenSongs = []

        songIndex = random.randrange(0, len(self.musiclist))
        while songIndex in self.chosenSongs: # Check if the song has already been chosen
            songIndex = random.randrange(0, len(self.musiclist))

        self.chosenSongs.append(songIndex)

        return self.musiclist[songIndex]
                

    """Handles the end of the game when the user has 0 lives"""
    def gameOver(self):
        print("Game over!")
        print()
        print("Final score: {}".format(self.score))

        print()
        print("Leaderboards")
        print()

        with open(LEADERBOARD_FILENAME, "r") as leaderboard_file:
            leaderboard = json.load(leaderboard_file)

        if self.username not in leaderboard or self.score > leaderboard[self.username]: # Check if user's score is higher than their leaderboard score (or it doesn't exist)
            print("New personal best!")

            leaderboard[username] = self.score
            

        keys = sorted(leaderboard, key=leaderboard.get, reverse=True)[:5] # Sort leaderboard dictionary and get the top 5 scores

        for k in keys:
            print("{}: {}".format(k, leaderboard[k])) # Print the username and the score in format "username: score"


        with open(LEADERBOARD_FILENAME, "w+") as leaderboard_file:
            json.dump(leaderboard, leaderboard_file) # Save updated leaderboard file

    """Create a new SongSession with a random song"""
    def newSongSession(self, song):
        print("-------------")
        print("Score: {}".format(self.score))        
        print(song.getHiddenName())

        self.session = SongSession(song, self)

        succeeded = self.session.guess()

        return succeeded

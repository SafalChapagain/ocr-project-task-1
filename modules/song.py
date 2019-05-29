"""Song class

Contains song and artist"""
class Song:
    def __init__(self, obj):
        self.artist = obj["artist"]
        self.name = obj["song"]

    """getHiddenName() -> string name
    Get song name with all letters except for the first of each word hidden

    E.G. song name Shape of You would return S___ o_ Y__"""

    def getHiddenName(self): 
        formatname = ""

        for word in self.name.split(" "):
            formatname += word[0] + (len(word) - 1) * "_" + " "
                
        return "{} - {}".format(self.artist, formatname)

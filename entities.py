# Main entities
# Defines the core classes.
#These are passive  objects that hold metadata (title, duration, genre, ratings). It also Includes logic for calculating the average rating.

class Song:
    def __init__(self, title: str, duration: int, genre: str, is_available:bool, ratings= list):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.is_available = is_available
        self.ratings = ratings
        
    def get_average (self):
        if not self.ratings:
            return 0 #0 in main.py will be transform to N/A.To keep N/A as default value. 
        average = sum (self.ratings)/ len (self.ratings)
        return round(average,1)

class Artiste: 
    def __init__(self, name: str, is_available:bool, songs: list):
        self.name= name
        self.is_available = is_available
        self.songs = songs #Composition, Artiste has a list of songs

        



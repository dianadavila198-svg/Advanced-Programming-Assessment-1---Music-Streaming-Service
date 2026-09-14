#Logic
#Manages the collection of Artistes and Songs. Handles loading/saving  from 'data.json', searching for songs, and the time-multiplier streaming logic. 

import json
import time
from entities import Song, Artiste #Import classes from entities

class StreamService:
    def __init__(self, time_multiplier=20):
        self.time_multiplier = time_multiplier
        self.catalogue = []

    def load_data(self):
        try:
            with open("storage.json", "r") as file: #Open JSON file 
                raw_data = json.load (file) #JSON file into a python variable/ list

            for artist_data in raw_data: #artist_data as dicionary
                songs_list = []

                #Song object creation
                for song_data in artist_data ['songs']: 
                    new_song = Song (   #referencing JSON with class
                        title = song_data['title'], 
                        duration = song_data['duration'],
                        genre= song_data['genre'],
                        is_available=song_data['is_available'],
                        ratings = song_data['ratings'], 
                        )
                    #Aggregating Song objects into a temporary list
                    songs_list.append(new_song)
                
                #Artiste object creation 
                new_artiste = Artiste ( #referencing JSON with class
                    name= artist_data ['artiste_name'],
                    is_available = artist_data ['is_available'],
                    songs = songs_list #Passing Song object to Artiste, Composition
                      )
                #Storing the complete Artiste object in the catalogue
                self.catalogue.append(new_artiste)

        except FileNotFoundError:
            print ("Error: The storage.json file was not found")

    #Filter and return a list of all available artist objects 
    def get_available_artistes(self):
        available_artist = [] #List to store matches
        for artist in self.catalogue:#iterate through each artist object 
            if artist.is_available:
                available_artist.append(artist)
        return available_artist
    
    # Find a specific artist and validate their available songs 
    #Returns UNAVAILABLE if the artist is disabled, a list of songs if active, or None if not found. 
    def get_songs_by_artiste (self, target_name):
        for artist in self.catalogue:
            if target_name.lower() in artist.name.lower():#Normalize strings to lowercase for user friendly search and use 'in' for partial matching
                #Check if the artist object is available 
                if not artist.is_available:
                    return "UNAVAILABLE"
                
                #If artist is available
                found_songs = []
                for song in artist.songs: #Access the Song objects within Artiste 
                    if song.is_available:
                        found_songs.append(song)
                        
                return found_songs #Return the list, even if empty. 
        
        #If the name is not found
        return None
    
    def stream_song (self, song, artiste_name):
        sleep_time = round(song.duration / self.time_multiplier, 2) #Print 2 positions for sleep time duration
        print(f"\n▶ Streaming now: {song.title} by {artiste_name}.")
        print (f"---Estimated streaming duration: {sleep_time} seconds--- \nEnjoy ♪ ♪ ♪")
        #Pause for simulating the stream
        time.sleep(sleep_time)
        print (f"Finished streaming {song.title} by {artiste_name}. Please give us a raiting on how you liked it.")

    def save_data (self):#Save object from python to JSON permanent list
        updated_data = [] #Dictionary to use
        for artist in self.catalogue:
            songs_to_save = []
            for song in artist.songs:
                song_dict= {
                    "title" :song.title, #Match JSON with Python object
                    "duration": song.duration, 
                    "genre":song.genre,
                    "is_available" :song.is_available,
                    "ratings" :song.ratings
                    }
                songs_to_save.append(song_dict)

            artiste_dic = {
                "artiste_name": artist.name, #Match JSON with Python object
                "is_available": artist.is_available,
                "songs" : songs_to_save,
                }
            updated_data.append(artiste_dic)

        with open("storage.json", "w") as file: #Open JSON file, "w" to have the latest version of JSON file 
            json.dump(updated_data, file, indent=4) #Save the list, indent=4 to organize it within JSON

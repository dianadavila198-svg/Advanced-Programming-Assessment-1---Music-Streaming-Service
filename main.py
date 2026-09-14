# User Interface
#This is the file used to launch the app.
#The main loop that interacts with the user via the console. 
#Displays the menu, captures inputs, and delegates actions to the StreamingService in service.py.

from service import StreamService #Import the logic of the program

#Create instance, Object to use within this file
my_streaming_program = StreamService()

#Call the filled/historic catalog 
my_streaming_program.load_data()

#Menu for End user
while True:
    print ("\n---♫ Welcome to the Music Streaming Service! ♫ ---")
    print ("\nPlease choose what action would you like to perform:")
    print(" 1. View Available Artistes (Browse)")
    print(" 2. Search, Play and Rate a Song (Stream)")
    print(" 3. View the Full Songs Collection & Artiste Ratings (Catalog)")
    print(" 4. Close the program")

    #Handle user input 
    choice = (input("\nEnter the number of your choice (1-4): ")) #Keep it open for string inputs, so the program doesnt crash on this phase. Error handle for invalid inputs after this line. 

    if choice not in ["1","2", "3", "4"]:
        print ("Invalid selection!")
        print ("Please enter a number between 1 and 4.")

    elif choice == "1":
        artistes = my_streaming_program.get_available_artistes() #Call te method via the instance
        if not artistes:
            print ("Not available artists at the moment")
        else:
            print (f"\n--- ♫ Available Artistes and their Songs ♫ ---")
            for artist in artistes:
                print(f"\nArtiste: {artist.name}")
                for song in artist.songs:
                    if song.is_available:
                        avg = song.get_average()
                        display_avg = f"{avg} ★" if avg > 0 else "N/A"
                        print(f"  - {song.title} ({song.genre}) | Avg: {display_avg}")

        input("\n--- Press Enter to return to the main menu ---")

    elif choice == "2":
        choice_2 =input ("\nPlease type the artist you would like to stream: ")
        specific_artist = my_streaming_program.get_songs_by_artiste(choice_2) #Pass the users input as the argument
        
        #Handle unavailable artists on catalogue. 
        if specific_artist == "UNAVAILABLE":
            print (f"\nSorry! The artist '{choice_2}' is currently unavailable in our service.")
            print ("Please try another search or try again later!")
            input("\n--- Press Enter to return to the main menu ---")

        #Handle not found status
        elif specific_artist is None:
            print (f"Our apologies! the artist {choice_2} is not in the catalogue.")
            input("\n--- Press Enter to return to the main menu ---")

        #Artist is found and available
        else:
            print (f"\nSongs found for {choice_2}:")
            for i, song in enumerate (specific_artist, 1):
                print(f"{i}. {song.title} ({song.genre})")
            try:
                song_choice = int(input("\nPlease enter the number of the song you would like to play: "))
                
                #Check if the number is withn the valid range of the list 
                if 1 <= song_choice <= len(specific_artist):
                    selected_song = specific_artist[song_choice - 1]#Access the object, Substract -1 as lists start on position 0
                    my_streaming_program.stream_song(selected_song, choice_2) #Access the method within service.py
                    
                    rating_loop = True
                    while rating_loop:
                        try:
                            new_rating = int(input("Please rate this song (1-5 scale): "))
                            if 1 <= new_rating <= 5: #Validate the input is within the scale permitted
                                selected_song.ratings.append(new_rating) #Update the object
                                my_streaming_program.save_data() #Save the rating wihin the permanent catalogue
                                print("\n★ Rating saved successfully! Thanks for visiting!")
                                rating_loop = False
                            else:
                                print ("Invalid input! Please enter a numerical rating (1-5)")

                        except ValueError:
                            print("Invalid input! Please enter a numerical rating (1-5)")

                else: #To handle higher int inputs that are not within the catalog 
                    print (f"Invalid selection. Please pick a number between 1 and {len(specific_artist)}")

            #To handle str inputs                
            except ValueError:
                print("Invalid input! Please enter the number of the song you want to play.")

            input("\n--- Press Enter to return to the main menu ---")

    elif choice == "3":
        print ("\n--- ♫ Full Music Catalogue ♫ ---")
        #Loop through every artist in the main catalogue list
        for artist in my_streaming_program.catalogue: #Access to the catalog within service.py
            status = "(Available)" if artist.is_available else "(Unavailable)" #is_available converted from boolean to str
            print (f"\nArtist: {artist.name} {status}")
            print (f"Songs: ")

            for song in artist.songs:
                avg= song.get_average()
                if avg == 0:
                    display_avg = "N/A"
                else:
                    display_avg = f"{avg} ★"
                
                print (f"- {song.title} | Average Rating: {display_avg}")

        input("\n--- Press Enter to return to the main menu ---")

    elif choice == "4":
        print ("\nClosing the Streaming Service...")
        print ("Thank you for listening!")
        print ("See you next time with more music! ♫")
        break
## Project 
Music Streaming Service

## Objective of the program
This program is a Python-based system designed to simulate a music streaming service using JSON as database. This program focus on Object-Oriented Programming (OOP) to organize artists and their songs. 
The goal is to allow users to browse available artists, search for specific catalogs of songs, and simulate a streaming experience with realistic wait times based on song duration.

## How to start?
**As a pre-requisite to execute this program, you need to have install Python 3 in your machine.**

## Download and execution of the program
1. Download the project folder and unzip it.(Once donwload, please make sure all the files are in the same folder)
2. Open your terminal or command prompt
3. ⁠type python main.py

## Structure of the code
The project follows a modular structure to keep the logic clean:

entities.py: Contains the Classes for Artiste and Song. This is where the core data structure and the average rating logic is.
service.py: The logic of the app. It handles loading data from JSON, filtering available artists, and the streaming timer math.
storage.json: Persistent database. It stores all the raw artist and song information. And make sure the data is not delete once the user close the session. 
main.py: The User Interface. This is the interactive menu where the user makes choices.

## How to use the program
Once the program starts, it is recommended to follow the flow 1 to 4 within the menu:

Option 1 (Browse): Shows list of ONLY available artists in the system. 
Option 2 (Stream & Rate): Search and choose a song by an specific Artiste, play it and rate at the end of the streaming. 
Option 3 (Full Catalogue): Show the complete library, Available and Unavailable Artistes. 
Option 4: Close the program. 

Note: please note this options available can be user in different order as well, for example choose 3 and then try to stream an Artist that is Unavailable, for this a handle error has been defined across the program. 

## PROJECT ARCHITECTURE

```text
.
├── entities.py              # Domain model classes (Artiste, Song, Composition & rating logic)
├── service.py               # Application logic (JSON loading, catalogue filters & streaming timer)
├── main.py                  # CLI user interface & interactive menu controller
├── storage.json             # Persistent JSON database (stores artist/song metadata & ratings)
└── README.md                # Project documentation
```

## How this program was tested?

After I finish the program, I spent significant time validating the different inputs a user could choose, to make sure the program works as expected, the testing was focus on:

Unit Testing: I checked single methods such as the average_rating function to make sure it returns "N/A" for songs with no ratings instead of crashing.
Search flexibility: I tested searching for just "olivia" or "dean." Thanks to the partial matching logic, it still finds the full name (Olivia Dean) and works even if you forget to use capital letters.
Error handling: I tested with random letters and simbols, and the try/except blocks catch this, showing the appropiate error messages. 
Unavailable artist: I intentionally set an artist to is_available: False in the JSON. I verified the system handles this by showing the correct "Unavailable" status messages.
Data Integrity: Verified that the JSON loader correctly builds "Composition" relationships (one artist holding multiple song objects).
Invalid inputs:In general I make sure the differnet error handling is all over the program, to avoid the system crashes on invalid inputs. 
User Experience: Some symbols, spaces and expressions were added to accomplish a better UX within the program. 

## Assumptions 
It is assumed that the storage.json file follows the specific nested structure (Artist -- Songs).
The time_multiplier is set to 20 by default to keep the "streaming" simulation fast enough for testing but slow enough to be realistic.

## Strategy executed for code development
Before writing any code, a system architecture diagram was drafted on paper to identify the key components of the project. This allowed for the clear definition of:

Project Structure: Organizing logic into separate files (Entities, Service, Main).
Objects: Defining classes, attributes, and methods.
Relationships: Mapping the Composition and Association between the Artiste and Song classes to ensure a data hierarchy.

## Additional notes
This project was built based on the lectures for the course CS551P - Advanced Programming, focusing on core topics of OOP such as:

Encapsulation: Ensuring that each class (Artiste and Song) manages its own internal data and logic, such as the calculation of average ratings.
Composition: Establishing a relationship where Artiste objects contain and manage a collection of Song objects.
Data Persistence: Implementing a JSON-based database to store and retrieve information. This ensures that historical user generated data (e.g.ratings) persists between program executions, rather than being lost when the session ends.

## Aditional references
I acknowledge the use of AI as a supportive tool for the following topics:

-Refinement of the final project structure (organizing logic across main.py, service.py, etc.). I drafted the initial structural framework and used AI to polish the separation of concerns.
-Assistance in identifying and resolving specific syntax errors and refining exception handling to improve system robustness.

## Author
**Diana Laura Davila Esparza 

 

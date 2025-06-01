# Use this file for your exercise solutions

# Q1- Write a function called display_message() that prints one sentence telling everyone what you are learning about in this module. Call the function, and make sure the message displays correctly
# def display_message():
#     print("I'm learning about functions in this module!")


# display_message()


# # Q2- Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as, “One of my favorite books is Alice in Wonderland.” Call the function, making sure to include a book title as an argument in the function call.


def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function with a book title
favorite_book("Harry Potter")


# Q3- Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"The shirt size is {size} and the message on it says: '{message}'")

# Call using **positional arguments**
make_shirt (size = "XXXL", message ="Mind the Gap")

# Call using **keyword arguments**
make_shirt(message="Avengers Assemble", size ="Medium")


def make_shirt(size, message):
    print(f"The shirt size is {size.upper()} and it will have the message: '{message}'.")

# Calling using positional arguments
make_shirt("medium", "Keep calm and code on.")

# Calling using keyword arguments
make_shirt(message="Eat. Sleep. Code. Repeat.", size="large")

# Stretch and Challenge version
def make_shirt(size="large", message="I love Python"):
    print(f"The shirt size is {size.upper()} and it will have the message: '{message}'.")

# Making a large shirt with default message
make_shirt()

# Making a medium shirt with default message
make_shirt(size="medium")

# Making a shirt with custom size and custom message
make_shirt(size="small", message="Debugging is my cardio.")



# Q-4 Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as, “Reykjavik is in Iceland.” Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(name, country):
    print(f"The place {name.upper()} is in {country.upper()}")


def describe_city(city, country="Iceland"):
    print(f"the {city} is in {country}.")

# Calling the function with three cities
describe_city("Reykjavik")            # Uses default country
describe_city("Akureyri")             # Uses default country
describe_city("Tokyo", "Japan")       # Overrides default country


# Q5- Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.

# **Advanced**:*Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.*


def make_album(artist, title, tracks=None):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album['tracks'] = tracks
    return album

# Creating three albums
album1 = make_album('pink floyd', 'the dark side of the moon')
album2 = make_album('radiohead', 'ok computer')
album3 = make_album('kendrick lamar', 'to pimp a butterfly', tracks=16)

# Printing album dictionaries
print(album1)
print(album2)
print(album3)

# While loop for user input
print("\nEnter album information. Type 'q' at any time to quit.")
while True:
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'q':
        break

    title = input("Enter the album title: ")
    if title.lower() == 'q':
        break

    tracks_input = input("Enter the number of tracks (optional): ")
    if tracks_input.lower() == 'q':
        break

    # Convert tracks to int if provided
    tracks = int(tracks_input) if tracks_input.isdigit() else None

    album = make_album(artist, title, tracks)
    print("Album created:", album)







# Kahdeim's Answer:
def make_album():
    while True:
        print("\nEnter the album details:")
 
        artist = input("Enter the artist (or type 'done' to exit): ")
        if artist.lower() == 'done':
            break
 
        title = input("Enter the album title: ")
 
        tracks_no = input("Enter the number of tracks (press Enter to skip): ")
        if tracks_no:
            tracks = int(tracks_no)
        else:
            tracks = "Not specified"
 
        album = {
            "artist": artist,
            "title": title
        }
        if tracks is not None:
            album["tracks"] = tracks
       
        print("\nAlbum created:")
        print(album)
        print(f"{artist.title()} - {title.title()} ({tracks})")
        break
 
make_album()
 
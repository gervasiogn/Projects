import os

# Function to extract place from filename
def extract_place(filename):
    return filename.split("_")[1]

# Make directories based on place name
def make_place_directories(places):
    for place in places:
        os.mkdir(place)

def organize_photos(directory):
    os.chdir(directory)
    # Filenames
    originals = os.listdir()
    places = []
    # Extract_Place function to extract names in directory 
    for filename in originals:
        place = extract_place(filename)
        places.append(place)

    make_place_directories(places)

    # Extract places names and move filename into respective folder 
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


# organize_photos("Photos")

print("TEST!")
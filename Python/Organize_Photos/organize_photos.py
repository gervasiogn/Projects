import os

# Function to extract place from filename
def extract_place(filename):
    return filename.split("_")[1]

def organize_photos(directory):
    os.chdir(directory)
    # Filenames
    originals = os.listdir()
    places = []
    # Call extract_place function to extract each place name 
    for filename in originals:
        place = extract_place(filename)
        # Append place name to places variable
        places.append(place)

# Make directories based on places variable 
def make_place_directories(places):
    # Use places variable to make directories
    for place in places:
        os.mkdir(place)

    make_place_directories(places)

    # Extract places names and move filename into respective folder 
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


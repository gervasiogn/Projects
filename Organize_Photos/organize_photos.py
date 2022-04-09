import os

def extract_place(filename):
    return filename.split('_')[1]

def make_place_directories(places): # Here's the function definition
    for place in places:
        os.mkdir(place)

os.chdir("Photos")
originals = os.listdir()
places = []
for filename in originals:
    place = extract_place(filename)
    places.append(place)

make_place_directories(places) # Don't forget to call the function!
print(os.listdir()) # Th
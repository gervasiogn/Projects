# Create a file in write mode and write to it

def write_to_file(filename):
    with open(filename, "w") as write:
        print("I created a new open file object to which I can write!")


write_to_file("new_write.txt")
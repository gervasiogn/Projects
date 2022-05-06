def write_to_file(filename):
    with open(filename, "w") as writefile:
        writefile.write("I created an open file object to which I can write!")

write_to_file("new_text.txt")
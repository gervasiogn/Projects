import string

these_words = ["lorem", "amet"]

def check_words(line):
    count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in these_words:
            count += 1
            print(f"The word: {word} was found!")
        return count


# Check file for specific words
def check_file(filename):
    with open(filename) as myFile:
        count = 0
        # Loop consumes file input one line at a time
        for line in myFile:
            count += check_words(line)
            if count == 0:
                print("None of those words were found")

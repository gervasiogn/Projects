import string

these_words = ["lorem", "amet"]

def check_line(line):
    count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in these_words:
            count += 1
            print(f"The word {word} was found")
    return count

def check_file(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            count += check_line(line)

    if count == 0:
        print("None of those words were found")



if __name__ == "check_words":
    check_file("copy.txt")

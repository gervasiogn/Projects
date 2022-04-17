# Create a file in write mode and write to it
writer = open("new_write.txt", "w")
for n in range(31):
    if n % 2 == 0:
        writer.write(f"{n}\n")

# Write(copy) the contents of one file to another
reader = open("read.txt")
copy = open("copy.txt", "w") 

copy.write(reader.read())
copy.close()


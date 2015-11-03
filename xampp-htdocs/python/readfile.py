# reads text in from a file

# w - open the file for writing (this deletes all existing content if the file already exists)
# r - open the file for reading
# a - open the file to append data to it (preserves existing data in the file)
def readFile1():
    with open("animals.txt", mode="r",encoding="utf-8") as myFile:
        for line in myFile:
            print(line.rstrip("\n")) # strips lines of new line character (\n)

def readFile2():
    with open("animals.txt", mode="r",encoding="utf-8") as myFile:
        animals = myFile.read().splitlines()
    for each in animals:
        print(each)
    animalToFind = input("What are you looking for?")
    if animalToFind in animals:
        print("Yes that's in the file.")
    else:
        print("Sorry, that's not in the file")

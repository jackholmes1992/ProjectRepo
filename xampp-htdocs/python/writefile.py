# writes information to a file

def writeToFile():
    animals = ["rat","frog","monkey"]
    with open("new_animals.txt", mode="w",encoding="utf-8") as my_file:
        for animal in animals:
            my_file.write(animal+"\n")

# This program will say hello to the user
# 2nd November

def main():
    print("What is your name?")
    yourName = input()
    print(yourName)
    print("Hello {0}!".format(yourName))
    #Ask what is age
    yourAge = int(input("What is your age?"))
    print("Hello {0}. You are a young {1}.".format(yourName,yourAge))

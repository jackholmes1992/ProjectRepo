import pickle

class audioTake(object):
    def __init__(self, take, curator):
        self.audioTake = take
        self.curator = curator

with open('audioTake.pkl', 'rb') as input:
    takeLoad = pickle.load(input)
##    print(takeLoad.audioTake)  # -> p
    print(takeLoad.curator)  # -> jack

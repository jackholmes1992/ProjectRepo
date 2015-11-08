#!/usr/local/bin/python3.5

import os
import json

def decode():
    jsonData = open("Session2.JSON")
    decodedData = json.load(jsonData)

    stringJson = decodedData
    print ("json data in readable form...</header>")
    print (str(json.dumps(stringJson, indent = 4)))

#main program
def main():
    decode()

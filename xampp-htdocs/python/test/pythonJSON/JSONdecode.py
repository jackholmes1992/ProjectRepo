#!/usr/local/bin/python3.5

import json

def decode():
    jsonData = open("Session2.JSON")
    decodedData = json.load(jsonData)
    print (json.dumps(decodedData, indent = 4))

def main():
    decode()
    

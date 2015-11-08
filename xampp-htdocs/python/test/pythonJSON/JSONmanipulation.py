#!/usr/local/bin/python3.5

import json



newEntry = {"clipId":"333333",
            "position":"00.00.00.00",
            "creator":"Laura"}
    
with open("Session2.JSON") as jsonData:

    #printing a JSON file
    decodedData = json.load(jsonData)
    print (json.dumps(decodedData, indent = 4))

    #adding a value
    tempList = decodedData["session"]
    tempList.append(newEntry)
    session = {"session":tempList}
    print (json.dumps(session, indent = 4))
    jsonData.close()
    
    #write back to original file
    with open('newSession.json', 'w') as newFile:
        json.dump(session, newFile)
    newFile.close()
    

    

  


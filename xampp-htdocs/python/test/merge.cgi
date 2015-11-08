#!/usr/local/bin/python3.5

import cgi
import os

def htmlTop():
    print("""Content-type:text/html\n\n
            <!DOCTYPE html>
            <html
        	<head lang="en">
            	    <meta charset="utf-8"/>
    		    <title>My Server-side template</title>
    		</head>
        	<body>""")

def htmlTail():
    print("""               </body>
            </html>""")

def merge():
    print("Merging .wav files... <br />")
    os.system("./sox -M PropellerEngine.wav Skid.wav 111111.wav ")
    print("...Files merged! <br />")

#main program
if __name__ == "__main__":
	try:
	    htmlTop()
	    merge()
	    htmlTail()
	except:
	    cgi.print_exception()

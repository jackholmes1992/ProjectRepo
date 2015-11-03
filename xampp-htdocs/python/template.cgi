#!/usr/local/bin/python3.5

import cgi

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

#main program
if __name__ == "__main__":
	try:
		htmlTop()
		print("Hello, world!")
		htmlTail()
	except:
		cgi.print_exception()

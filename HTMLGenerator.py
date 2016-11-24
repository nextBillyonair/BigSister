import cv2
import numpy as np 

# Maybe use reactJS?


def html(filename):

	with open("%s" % filename, 'w') as writer:
		writer.write("<!DOCTYPE html>\n")		
		writer.write("<html>\n")
		header(writer)
		body(writer)
		writer.write("</html>")



def header(writer):
	writer.write("<head>\n")
	title(writer, "JHU ACM Office Door Camera")

	writer.write("</head>\n")


def title(writer, string):
	writer.write("<title>\n")
	writer.write("%s\n" % string)
	writer.write("</title>\n")


def body(writer):
	pass


def comment(writer, com):
	writer.write("<!-- %s -->\n" % com)



"""
		<!DOCTYPE html>
<html>
<head>
<!-- HTML Codes by Quackit.com -->
<title>
JHU ACM Office Door Data</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Data retrieved from processing the images from the Office Door camera.">
<style>
body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{font-family:Arial, sans-serif;color:#000000;background-color:#ffffff;}
p {font-family:Georgia, serif;font-size:14px;font-style:normal;font-weight:normal;color:#000000;background-color:#ffffff;}
</style>
</head>
<body>
<h1></h1>
<p></p>
</body>
</html>
"""
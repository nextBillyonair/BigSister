# BigSister
This project will use OpenCV to count the number of people in the ACM at any one time. The information will be accessible via the IRC through a bot. The bot will also record the amount of people in the ACM over time to record statistics and  predict future attendance levels.


# Contributors
William Watson wwatso13@jhu.edu billyonair

Joshan Bajaj jbajaj1@jhu.edu jbajaj


# Journal Notes -> Bill
## Note 12
Move code around a bit, streamlined main file. Also segments the motion and only looks at parts where there are motion, however it iterprets the entire frame as one object, so i will look into connected components with mutual marriages to resolve this.

## Note 11
Hard coded an HTML file with embedded CSS and JavaScript to allow for 
a nice GUI to display some results. It also auto refreshes the images via
the JavaScript embedded code. Next part: fixing motion detect to reduce number of 
Rectangles produced then slicing that ROI to interpret Flow derivatives. This will allow 
Is to avoid the motion that is not really moving while also easily tell us where objects are
Moving to. Now just need to write data to object and create pretty graphs to view in HTML file. 
Also need to talk to Joshan on Bot integration and how he wants them to integrate. 
Happy Thanksgiving ;)
## Note 10
Cleaned up the Optical Flow classes. Moved around methods in motion detect. New
file for rectangle interpretation methods. Combo of motion detect and optical 
flow is being considered now. In addition, still need to look into reactJS.

## Note 9
Looking into ReactJS for HTML generation. 

## Note 8
After going to CV, we talked about Optical Flow, which can track movement in an image. My idea here is for the motion detect to get ROIs from our image, and use the fx fy from opti-flow to see if any reasonable change is occuring. IE filter out noise vs actual objects. This is the current plan until I change my mind. As always, will 
modularize and keep if it fails.

## Note 7
I may want to include a HTML file to display my results, where a program could write to an HTML file from python, using images colelcted from this tracking problem.
I think of it as a user friendly results page to tell us how we are doing in a reasonable way. Would like to host it permanently on the ACM website.

## Note 6
Quickly added SaveLoad.py, which contains two useful functions to save and load binary files using pickle. This will allow us to save binary object files and quickly 
reload them, allowing persistance for the duration of time. We plan to save our histograms and data in object files to faciliate easier and faster computation.

## Note 5
After some thought I decided to expand this project to include extra useful CV methods to make them readily and easily availbe in case of use. While some of these
methods may never be used, it is always good to have them around. So I made the gradient module, ImageIO module, etc for ease of use. Also I will keep any failed 
attempts at tracking in case anyone else would like to use the modules for a different project in the future.

## Note 4
I looked into simple tracking algorithms and ideas. One possiblity is to take the absolute differnce of the images, then apply a simple binary threshold. 
Then draw the bounding rectangle. Problems: Requires base image, only looks at difference so any moved object is forever considerd motion. 
Benefits: Super fast and simple, provides reasonable results with good lighting and base image. Will explore further.  

## Note 3
Also, started by creating an object for face detection to reduce code duplication
and to make main file more readable. It works well in discovering faces and drawing a bounding rectangle when the face in directly in front
of the camera, however it fails to detect the profile of the face or the back of the head. Face detection may not solve our problem, and may be too
limited in its uses for simple tracking.

## Note 2
Started to play around with the ACM cameras currently located in the office. So two URL camera objects were
made to hijack the feed from the cams. Using urllib, we sucessfully fetched the images and displayed them to the screen.

## Note 1
At first We made objects to hold the cameras so that we could acess them easily.
Two types exists: URL and Web. URL fetches an image from a stream from a given address.
Web takes the feed from a pluged in camera and controls the flow of info from it.


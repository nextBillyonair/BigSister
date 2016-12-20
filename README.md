# BigSister
This project will use OpenCV to count the number of people in the ACM at any one time. The information will be accessible via the IRC through a bot. The bot will also record the amount of people in the ACM over time to record statistics and  predict future attendance levels.


# Contributors
William Watson wwatso13@jhu.edu billyonair

Joshan Bajaj jbajaj1@jhu.edu jbajaj


# Journal Notes

## Note 17
I added functionality to return the current officers with 
their email addresses and names since it was a requested
feature. I also wrote the predict people method. This took
quite a while to program because of parsing and rounding issues,
but I finally have a product that can predict if it has enough
data. For now, I haven't included days of the week as part of the
prediction since Marc warned against it for now. He feels that 
we'll need much more data before it makes sense to program that
functionality, and for now it is just important to have a predict
based off of the time of day. Additionally, I got some more requests
from IRC members --> 1) Make a way to return the meeting blurb onto 
the IRC channel, and 2) Get information on a given acm username.
Both seem like achievable tasks, but number 1 would require someone
to update the blurb's textfile weekly. Marc mentioned that he is working
on something to do that in the future, so I will check in with him on that.
Speaking of Marc, he wants to add some security features to the bot before 
goes online, so once he does that, this project will be able to go live!

To summarize what I learned about IRC programming from this project is that
there are many conditions that I have to keep in mind when writing irc code
that I normally don't have to think about when writing regular code. For 
example, sending simple print statements to the channel requires quite a bit
of tinkering, especialyl when you want it to go to a specific user. Also, 
flooding and character limits have to constantly be kept in mind. A huge part
of the work was in parsing the data strings, since they all contained various
amounts of IRC junk but also very different commands. Speaking of commands, 
I learned how important it is to think of good names for them because of how
difficult it was for Bill to use my bot when I asked him to test it. I learned
that I needed to make the command names more intuitive so that it's more user
friendly. I spent a good deal of time playing with the names until I thought
they were more user friendly, but the real test will be when the bot goes 
online in the main channel. I'll be monitoring to see what 'mistakes' people
will make when using the bot, so that I can handle them and do what the user
wanted to do in the first place. 

## Note 16
I added the code that gives the sysadmin notes on the IRC. 
I made use of urllib2 and I then parsed the html to get the data that I needed,
but figuring out where the data I needed was hidden among the HTML took quite a bit.
Another barrier I ran into was printing too many characters in a message, 
so I had to find a way to break up the notes into seperate groups.
I also did some testing to figure out how to private message IRC
messages so that the main channel isn't spammed. I'm happy with the 
finished note return product. 

## Note 15
I wrote the code that returns how many people are currently in the ACM
after working with Bill. I also wrote the help functions, and learned 
about IRC flooding. I'm now making use of the time.sleep() function so
that flooding is no longer an issue, just an annoyance that I need to look
out for. 

## Note 14
Move code around a bit, streamlined main file. Also segments the motion and only looks at parts where there are motion, however it iterprets the entire frame as one object, so i will look into connected components with mutual marriages to resolve this.

## Note 13
Hard coded an HTML file with embedded CSS and JavaScript to allow for 
a nice GUI to display some results. It also auto refreshes the images via
the JavaScript embedded code. Next part: fixing motion detect to reduce number of 
Rectangles produced then slicing that ROI to interpret Flow derivatives. This will allow 
Is to avoid the motion that is not really moving while also easily tell us where objects are
Moving to. Now just need to write data to object and create pretty graphs to view in HTML file. 
Also need to talk to Joshan on Bot integration and how he wants them to integrate. 
Happy Thanksgiving ;)

## Note 12
I cleaned up the existing irc code to move towards a method oriented design. 
At admin's meeting, I was given a few requests for methods/functionality 
to add to the bot. The most requested one by far was returning 
admins' notes on IRC. I've started discussing with Marc how can get the 
information I need off of the webpages to make the request a reality.
I also wrote some code to make exiting less dangerous, and I added some 
code to accept some less exact commands from the user by making use of
the "re" library. 

## Note 11
Cleaned up the Optical Flow classes. Moved around methods in motion detect. New
file for rectangle interpretation methods. Combo of motion detect and optical 
flow is being considered now. In addition, still need to look into reactJS.

## Note 10
Looking into ReactJS for HTML generation. 

## Note 9
After going to CV, we talked about Optical Flow, which can track movement in an image. My idea here is for the motion detect to get ROIs from our image, and use the fx fy from opti-flow to see if any reasonable change is occuring. IE filter out noise vs actual objects. This is the current plan until I change my mind. As always, will 
modularize and keep if it fails.

## Note 8
I may want to include a HTML file to display my results, where a program could write to an HTML file from python, using images colelcted from this tracking problem.
I think of it as a user friendly results page to tell us how we are doing in a reasonable way. Would like to host it permanently on the ACM website.

## Note 7
I began work on the IRC bot. It was quite a challenge to get it working with freenode irc as 
I had trouble finding the host name. Once I got the bot to connect to the irc, 
I made a few very basic commands to test out. I've been testing my bot in the
'#joshtest' IRC channel so that I don't spam the main IRC channel. 
Writing code that is IRC friendly is very difficult as it requires very exact writing.
I also added the ability to check the ACM webcams for a livefeed.

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


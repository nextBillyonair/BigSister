import socket
import re
import pickle
import urllib2
import time
import os
import csv
import math

#Global variables
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
global milkcount
global dataTime
global notesDic
global officerEmails
global officerNames
global officerOrder

#Sets up the IRC for the rest of the program
def setUpIRC():
   global milkcount
   global dataTime
   network = 'irc.freenode.net'
   port = 6667
   irc.connect ( ( network, port ) )
   print irc.recv ( 4096 )
   irc.send ( 'NICK botty\r\n' )
   irc.send ( 'USER botty botty botty :Python IRC\r\n' )
   irc.send ( 'JOIN #joshtest\r\n' )
   irc.send ( 'PRIVMSG #joshtest :Hello World.\r\n' )
   irc.send("PRIVMSG #joshtest :For a list of my commands, type '!botty help'\r\n")
   try:
      with open("milk.p", "rb") as m:
         milkcount = pickle.load(open("milk.p", "rb"))
   except IOError:
      milkcount = 0
   '''
   try:
      with open("dataTime.p", "rb") as d:
         dataTime = pickle.load(open("dataTime.p", "rb"))
   except IOError:
      dataTime = {}
   '''

#Method that runs fo the majority of the program's run time, reads the irc messages
def runIRC():
   global milkcount
   global notesDic
   timer = time.time()
   while True:
      if time.time() - timer > 600:
         timer = time.time()
         irc.send("PRIVMSG #joshtest :For a list of my commands, type '!botty help'\r\n")
      data = irc.recv ( 4096 )
      if re.search('PING', data, re.IGNORECASE):
         irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
      if re.search('!botty quit', data, re.IGNORECASE):
         irc.send ( 'PRIVMSG #joshtest :Fine, if you dont want me\r\n' )
         irc.send ( 'QUIT\r\n' )
         break
      if re.search('hi botty', data, re.IGNORECASE):
         irc.send ( 'PRIVMSG #joshtest :I already said hi...\r\n' )
      if re.search("!help botty -fun", data, re.IGNORECASE) or re.search("!botty help -fun", data, re.IGNORECASE):
         helpInstructionsFun()
      elif re.search("!help botty -all", data, re.IGNORECASE) or re.search("!botty help -all", data, re.IGNORECASE):
         helpInstructionsAll()
      elif re.search("!help botty", data, re.IGNORECASE) or re.search("!botty help", data, re.IGNORECASE):
         helpInstructions()
      if re.search("botty predict", data, re.IGNORECASE):
         predictPeople(data)
      if re.search("botty people", data, re.IGNORECASE):
         getPeople()
      if re.search('hello botty', data, re.IGNORECASE):
         irc.send ( 'PRIVMSG #joshtest :I already said hi...\r\n' )
      if re.search('botty officers', data, re.IGNORECASE):
         foundKey = False
         for element in officerOrder:
            if re.search("botty officers " + element, data, re.IGNORECASE):
               returnOfficer(element)
               foundKey = True
         if foundKey == False:
            getOfficers(data)
      if re.search('KICK', data, re.IGNORECASE):
         irc.send ( 'JOIN #joshtest\r\n' )
      if re.search("botty notes", data, re.IGNORECASE):
         foundNote = False
         for element in notesDic:
            if re.search("botty notes " + element, data, re.IGNORECASE):
               getNote(element)
               foundNote = True
         if re.search("botty notes -titles", data, re.IGNORECASE) or re.search("botty notes -title", data, re.IGNORECASE):
            noteOptions(data)
            foundNote = True
         if foundNote == False and re.search("botty notes\r\n", data, re.IGNORECASE):
            giveNotes(data)
         elif foundNote == False:
            irc.send("PRIVMSG #joshtest :Command not recognized. Try 'botty notes' for a the full list of notes, 'botty notes -title' for a list of note titles, or 'botty notes [TITLE HERE]' for an individual note entry\r\n")
      if re.search("cheese", data, re.IGNORECASE):
         irc.send ( 'PRIVMSG #joshtest :WHERE!!!!!!\r\n' )
      if re.search("milk", data, re.IGNORECASE):
         milkcount += 1
         if milkcount == 1:
            irc.send ( "PrIVMSG #joshtest :I've now drunk " + str(milkcount) + " gallon of milk\r\n")
         else:
            irc.send ( "PrIVMSG #joshtest :I've now drunk " + str(milkcount) + " gallons of milk\r\n")
      if re.search('slaps botty', data, re.IGNORECASE):
         irc.send ( 'PRIVMSG #joshtest :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n')
      if re.search('botty acm', data, re.IGNORECASE):
         irc.send("PRIVMSG #joshtest :http://polaris.acm.jhu.edu/\r\n")
         #irc.send( 'PrIVMSG #joshtest :http://polaris.acm.jhu.edu/motion/thread2/lastimage.jpg?time=1474063328843\r\n PrIVMSG #joshtest :http://polaris.acm.jhu.edu/motion/thread1/lastimage.jpg?time=1474064133272\r\n')
      print data

# Returns all of the help instructions
def helpInstructionsAll():
   irc.send('PRIVMSG #joshtest :This bot was designed to help monitor the number of people in G-67.\r\n')
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type '!help botty' or '!botty help' to get instructions on how to use the useful commands only.\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Add a '-fun' tag to get the instructions for fun commands only.\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Add a '-all' tag to get all of the instructions for every command.\r\n")
   time.sleep(1)
   irc.send('PRIVMSG #joshtest :Here are the commands you can use--\r\n')
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'hi botty' or 'hello botty' to say hi to me\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'milk' to make me drink some milk\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'slaps botty' to get in some trouble\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'cheese' to make me hunt for cheese\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty acm' to see the acm live\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty people' to get a count on how many people are in G-67\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty notes' to get the SysAdmin notes messaged directly to you\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty notes [TITLE HERE]' to return a specific SysAdmin note\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty notes -title' to get the list of SysAdmin note titles messaged to you\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty officers' to get the list of officers and their email addresses sent to you\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty officers [POSITION HERE]' to get that officer's name and email address\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty predict hh:mm' to get a prediction of how many people will be in G-67 at a given data and time. Note, we are still gather data for this method.\r\n")

# Returns the fun help instructions
def helpInstructionsFun():
   irc.send('PRIVMSG #joshtest :This bot was designed to help monitor the number of people in G-67, but it also has fun commands.\r\n')
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type '!help botty' or '!botty help' to get instructions on how to use the useful commands only.\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Add a '-all' tag to get all of the instructions for every command.\r\n")
   time.sleep(1)
   irc.send('PRIVMSG #joshtest :Here are the fun commands you can use--\r\n')
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'hi botty' or 'hello botty' to say hi to me\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'milk' to make me drink some milk\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'slaps botty' to get in some trouble\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'cheese' to make me hunt for cheese\r\n")

# Returns the help instructions
def helpInstructions():
   irc.send('PRIVMSG #joshtest :This bot was designed to help monitor the number of people in G-67.\r\n')
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type '!help botty' or '!botty help' to get instructions on how to use the useful commands only.\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Add a '-fun' tag to get the instructions for fun commands only.\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Add a '-all' tag to get all of the instructions for every command.\r\n")
   time.sleep(1)
   irc.send('PRIVMSG #joshtest :Here are the commands you can use--\r\n')
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty acm' to see the acm live\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty people' to get a count on how many people are in G-67\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty notes' to get the SysAdmin notes messaged directly to you\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty notes [TITLE HERE]' to return a specific SysAdmin note\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty notes -title' to get the list of SysAdmin note titles messaged to you\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty officers' to get the list of officers and their email addresses sent to you\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty officers [POSITION HERE]' to get that officer's name and email address\r\n")
   time.sleep(1)
   irc.send("PRIVMSG #joshtest :Type 'botty predict hh:mm' to get a prediction of how many people will be in G-67 at a given data and time. Note, we are still gathering data for this method.\r\n")

# Sets up the dataTime dictionary for predicting
def setupPeople():
   global dataTime
   people = open("people.txt", 'r')
   for line in people:
      lineLoc = line.find('|')
      numPeople = line[lineLoc + 1:].strip('\n')
      dateTime = line[:lineLoc]
      commaLoc = dateTime.find(',')
      date = dateTime[:commaLoc]
      time = dateTime[commaLoc + 1:]
      timeShort = time[:-3]
      minutesCol = timeShort.find(':')
      minutes = int(timeShort[minutesCol+1:])
      minutes = int(round(minutes, -1))
      if minutes == 0:
         minutes = "00"
      else:
         minutes = str(minutes)
      timeShort = timeShort[:minutesCol] + ":" + minutes
      if timeShort not in dataTime:
         dataTime[timeShort] = [int(numPeople)]
      else:
         dataTime[timeShort].append(int(numPeople))
   people.close()

# Predicts the number of people that will be in G-67 at a given time
def predictPeople(message):
   global dataTime
   dataTime = {}
   setupPeople()
   timeLoc = message.find("botty predict ")
   timeLen = len("botty predict ")
   time = message[timeLoc+timeLen:].strip('\r')
   time = time.strip('\n')
   if ':' not in time:
      irc.send("PRIVMSG #joshtest :Please submit your request in the following format: 'botty predict hh:mm'\r\n")
      return
   minutesCol = time.find(':')
   minutes = int(time[minutesCol+1:])
   minutes = int(round(minutes, -1))
   if minutes == 0:
      minutes = "00"
   else:
      minutes = str(minutes)
   time = time[:minutesCol] + ":" + minutes
   if time not in dataTime:
      irc.send("PRIVMSG #joshtest :Please submit your request in the following format: 'botty predict hh:mm'\r\n")
      return
   else:
      length = len(dataTime[time])
      sumPeople = 0
      for element in dataTime[time]:
         sumPeople += element
      numPeople = float(sumPeople) / float(length)
      numPeople = round(numPeople, 1)
      irc.send("PRIVMSG #joshtest :We predict that " + str(numPeople) + " will be in G-67 at " + time +"\r\n")
   irc.send("PRIVMSG #joshtest :More will be written soon to allow day predictions as well\r\n")

# Gets the number of people that were in G-67 most recently
def getPeople():
   people = open("people.txt", 'r')
   for line in people:
      pass
   lineLoc = line.find('|')
   numPeople = line[lineLoc + 1:].strip('\n')
   dateTime = line[:lineLoc]
   commaLoc = dateTime.find(',')
   date = dateTime[:commaLoc]
   time = dateTime[commaLoc + 1:]
   irc.send("PRIVMSG #joshtest :The number of people in G-67 at " + time + " on " + date + " was " + numPeople + " people.\r\n")
   people.close()

# Sends all of the admin notes to a user in a private message
def giveNotes(message):
   global notesDic
   endNameloc = message.find("!")
   name = message[1:endNameloc]
   urlshort = "https://www.acm.jhu.edu/~admins.pub/systems/"
   irc.send("PRIVMSG #joshtest :Full list of notes are being private messaged to " + name + "\r\n")
   irc.send("PRIVMSG #joshtest :Please wait " + str(len(notesDic)) + " seconds before giving me another command\r\n")
   irc.send("PRIVMSG " + name + " :hello " + name + "! Here are the list of notes I can give you\r\n")
   neededLines = open("neededLines.txt", 'r')
   for line in neededLines:
      startPos = line.find('ml">')
      endPos = line.find('</a')
      note = line[startPos+4:endPos]
      note = note.replace('&#8217;', "'")
      hrefLoc = line.find('href')
      noteurl = urlshort+ line[hrefLoc+6:startPos+2]
      if 'toctree-l1' in line:
         irc.send("PRIVMSG " + name + " : " + note + ": " + noteurl + "\r\n")
      elif 'toctree-l2' in line:
         irc.send("PRIVMSG " + name + " : --" + note + ": " + noteurl + "\r\n")
      elif 'toctree-l3' in line:
         irc.send("PRIVMSG " + name + " : ----" + note + ": " + noteurl + "\r\n")
      elif 'toctree-l4' in line:
         irc.send("PRIVMSG " + name + " : ------" + note + ": " + noteurl + "\r\n")
      elif 'toctree-l5' in line:
         irc.send("PRIVMSG " + name + " : --------" + note + ": " + noteurl + "\r\n")
      time.sleep(1)
   neededLines.close()

# Prints a given admin note to the IRC channel
def getNote(note):
   global notesDic
   irc.send("PRIVMSG #joshtest :Here are the notes for " + note + " --> " + notesDic[note] + "\r\n")

# Sends the titles of all of the admin notes to the user in a private message
def noteOptions(message):
   global notesDic
   endNameloc = message.find("!")
   name = message[1:endNameloc]
   numNotes = len(notesDic)
   arrKeys = []
   i = 0
   numKey = 0
   for key in notesDic:
      if numKey == 0:
         arrKeys.append([key])
         numKey += 1
      else:
         arrKeys[i].append(key)
         numKey += 1
      if numKey == 8:
         numKey = 0
         i += 1
   irc.send("PRIVMSG #joshtest :The list of available notes is being private messaged to " + name + "\r\n")
   irc.send("PRIVMSG " + name + " :These are all of the available notes:\r\n")
   start = 1
   end = start + 7
   for element in arrKeys:
      strTitles = str(element).strip('[')
      strTitles = strTitles.strip(']')
      irc.send("PRIVMSG " + name + " :Titles " + str(start) + " through " + str(end) + ": "+ strTitles + "\r\n")
      start = end + 1
      end = end + 8
      if end > numNotes:
         end = numNotes
      time.sleep(1)
   irc.send("PRIVMSG " + name + " :To get the notes for one of these, please type 'botty notes [TITLE HERE]'\r\n")

# Sets up the dictionaries and array for officers
def setupOfficers():
   global officerNames
   global officerEmails
   global officerOrder
   officerNames = {}
   officerEmails = {}
   officerOrder = []
   c = open("officerInfo.csv")
   csv_c = csv.reader(c)
   for line in csv_c:
      officerNames[line[0]] = line[1]
      officerEmails[line[0]] = line[2]
      officerOrder.append(line[0])

# Sends the list of officers and email addresses to the user in a private message
def getOfficers(message):
   global officerNames
   global officerEmails
   global officerOrder
   endNameloc = message.find("!")
   name = message[1:endNameloc]
   irc.send("PRIVMSG #joshtest :List of officers being sent privately to " + name + "\r\n")
   irc.send("PRIVMSG " + name + " :The officers are as follows:\r\n")
   i = 0
   for element in officerOrder:
      time.sleep(1)
      irc.send("PRIVMSG " + name + " :" + officerOrder[i] + ": " + officerNames[officerOrder[i]] + " (" + officerEmails[officerOrder[i]] + ")\r\n")
      i += 1
   irc.send("PRIVMSG " + name + " :To email all of officers, please email 'officers@acm.jhu.edu'\r\n")

# Prints the given officer's name and email to the channel
def returnOfficer(title):
   global officerNames
   global officerEmails
   irc.send("PRIVMSG #joshtest :Here is the information on the " + title + ": " + officerNames[title] + " (" + officerEmails[title] + ")\r\n")
   irc.send("PRIVMSG #joshtest :To email all officers, please email 'officers@acm.jhu.edu'\r\n")

# Creates the notes dictionary
def buildNotes():
   global notesDic
   notesDic = {}
   url = "https://www.acm.jhu.edu/~admins.pub/systems/index.html"
   urlshort = "https://www.acm.jhu.edu/~admins.pub/systems/"
   f = urllib2.urlopen(url)
   htmlRaw = open("htmlRaw.txt", 'w')
   htmlRaw.write(f.read())
   htmlRaw.close()
   htmlRaw = open("htmlRaw.txt", 'r')
   neededLines = open("neededLines.txt", 'w')
   for line in htmlRaw:
      if 'li class="toctree' in line:
         neededLines.write(line)
   htmlRaw.close()
   neededLines.close()
   neededLines = open("neededLines.txt", 'r')
   for line in neededLines:
      startPos = line.find('ml">')
      endPos = line.find('</a')
      note = line[startPos+4:endPos]
      note = note.replace('&#8217;', "'")
      hrefLoc = line.find('href')
      noteurl = urlshort+ line[hrefLoc+6:startPos+2]
      notesDic[note] = noteurl
   neededLines.close()
   os.remove("htmlRaw.txt")

# Runs the program
if __name__ == '__main__':
   buildNotes()
   setupOfficers()
   setUpIRC()
   runIRC()
   print("Safely exited")
   pickle.dump(milkcount, open("milk.p", "wb"))
   #pickle.dump(dataTime, open("dataTime.p", "wb"))
   os.remove("neededLines.txt")
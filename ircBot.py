import socket
import re
import pickle

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
global milkcount
global dataPeople

def setUpIRC():
   global milkcount
   global dataPeople
   network = 'irc.freenode.net'
   port = 6667
   irc.connect ( ( network, port ) )
   print irc.recv ( 4096 )
   irc.send ( 'NICK botty\r\n' )
   irc.send ( 'USER botty botty botty :Python IRC\r\n' )
   irc.send ( 'JOIN #joshtest\r\n' )
   irc.send ( 'PRIVMSG #joshtest :Hello World.\r\n' )
   try:
      with open("milk.p", "rb") as m:
         milkcount = pickle.load(open("milk.p", "rb"))
   except IOError:
      milkcount = 0
      '''
   try:
      with open("dataPeople.p", "rb") as d:
         dataPeople = pickle.load(open("dataPeople.p", "rb"))
   except IOError:
      dataPeople = {}
'''

def runIRC():
   global milkcount
   while True:
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
      if re.search('hello botty', data, re.IGNORECASE):
         irc.send ( 'PRIVMSG #joshtest :I already said hi...\r\n' )
      if re.search('KICK', data, re.IGNORECASE):
         irc.send ( 'JOIN #joshtest\r\n' )
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
      if re.search('Show me the acm', data, re.IGNORECASE):
         irc.send("PRIVMSG #joshtest :http://polaris.acm.jhu.edu/\r\n")
         #irc.send( 'PrIVMSG #joshtest :http://polaris.acm.jhu.edu/motion/thread2/lastimage.jpg?time=1474063328843\r\n PrIVMSG #joshtest :http://polaris.acm.jhu.edu/motion/thread1/lastimage.jpg?time=1474064133272\r\n')
      print data

def helpInstructionsAll():
   irc.send('PRIVMSG #joshtest :This bot was designed to help monitor the number of people in G-67.\r\n')
   irc.send("PRIVMSG #joshtest :Type '!help botty' or '!botty help' to get instructions on how to use the useful commands only.\r\n")
   irc.send("PRIVMSG #joshtest :Add a '-fun' tag to get the instructions for fun commands only.\r\n")
   irc.send("PRIVMSG #joshtest :Add a '-all' tag to get all of the instructions for every command.\r\n")
   irc.send('PRIVMSG #joshtest :Here are the commands you can use--\r\n')
   irc.send("PRIVMSG #joshtest :Type 'hi botty' or 'hello botty' to say hi to me\r\n")
   irc.send("PRIVMSG #joshtest :Type 'milk' to make me drink some milk\r\n")
   irc.send("PRIVMSG #joshtest :Type 'slaps botty' to get in some trouble\r\n")
   irc.send("PRIVMSG #joshtest :Type 'cheese' to make me hunt for cheese\r\n")
   irc.send("PRIVMSG #joshtest :Type 'show me the acm' to see the acm live\r\n")
   irc.send("PRIVMSG #joshtest :Type 'botty people' to get a count on how many people are in G-67\r\n")
   irc.send("PRIVMSG #joshtest :Type 'botty predict' to get a prediction of how many people will be in G-67 at a given data and time\r\n")

def helpInstructionsFun():
   irc.send('PRIVMSG #joshtest :This bot was designed to help monitor the number of people in G-67, but it also has fun commands.\r\n')
   irc.send("PRIVMSG #joshtest :Type '!help botty' or '!botty help' to get instructions on how to use the useful commands only.\r\n")
   irc.send("PRIVMSG #joshtest :Add a '-all' tag to get all of the instructions for every command.\r\n")
   irc.send('PRIVMSG #joshtest :Here are the fun commands you can use--\r\n')
   irc.send("PRIVMSG #joshtest :Type 'hi botty' or 'hello botty' to say hi to me\r\n")
   irc.send("PRIVMSG #joshtest :Type 'milk' to make me drink some milk\r\n")
   irc.send("PRIVMSG #joshtest :Type 'slaps botty' to get in some trouble\r\n")
   irc.send("PRIVMSG #joshtest :Type 'cheese' to make me hunt for cheese\r\n")

def helpInstructions():
   irc.send('PRIVMSG #joshtest :This bot was designed to help monitor the number of people in G-67.\r\n')
   irc.send("PRIVMSG #joshtest :Type '!help botty' or '!botty help' to get instructions on how to use the useful commands only.\r\n")
   irc.send("PRIVMSG #joshtest :Add a '-fun' tag to get the instructions for fun commands only.\r\n")
   irc.send("PRIVMSG #joshtest :Add a '-all' tag to get all of the instructions for every command.\r\n")
   irc.send('PRIVMSG #joshtest :Here are the commands you can use--\r\n')
   irc.send("PRIVMSG #joshtest :Type 'show me the acm' to see the acm live\r\n")
   irc.send("PRIVMSG #joshtest :Type 'botty people' to get a count on how many people are in G-67\r\n")
   irc.send("PRIVMSG #joshtest :Type 'botty predict' to get a prediction of how many people will be in G-67 at a given data and time\r\n")

def predictPeople():
   global dataPeople




setUpIRC()
runIRC()
print("Safely exited")
pickle.dump(milkcount, open("milk.p", "wb"))

import socket
import re
import pickle

network = 'irc.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK botty\r\n' )
irc.send ( 'USER botty botty botty :Python IRC\r\n' )
irc.send ( 'JOIN #joshtest\r\n' )
irc.send ( 'PRIVMSG #joshtest :Hello World.\r\n' )
try:
   with open("milk.p", "rb") as m:
      milkcount = pickle.load(open("milk.p", "rb"))
      print("heyo")
except IOError:
   print("hey")
   milkcount = 0
strcheese = "cheese"
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
   if re.search('hello botty', data, re.IGNORECASE):
      irc.send ( 'PRIVMSG #joshtest :I already said hi...\r\n' )
   if re.search('KICK', data, re.IGNORECASE):
      irc.send ( 'JOIN #joshtest\r\n' )
   if re.search(strcheese, data, re.IGNORECASE):
      irc.send ( 'PRIVMSG #joshtest :WHERE!!!!!!\r\n' )
   if re.search("milk", data, re.IGNORECASE):
      milkcount += 1
      if milkcount == 1:
         irc.send ( "PrIVMSG #joshtest :I've now drunk " + str(milkcount) + " gallon of milk\r\n")
      else:
         irc.send ( "PrIVMSG #joshtest :I've now drunk " + str(milkcount) + " gallons of milk\r\n")
   if re.search('slaps botty', data, re.IGNORECASE):
      irc.send ( 'PRIVMSG #joshtest :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.')
   if re.search('Show me the acm', data, re.IGNORECASE):
      irc.send( 'PrIVMSG #joshtest :http://polaris.acm.jhu.edu/motion/thread2/lastimage.jpg?time=1474063328843\r\n PrIVMSG #joshtest :http://polaris.acm.jhu.edu/motion/thread1/lastimage.jpg?time=1474064133272\r\n')
   print data

pickle.dump(milkcount, open("milk.p", "wb"))

print("Safely exited")
#!/usr/bin/env python2.7
#
# Example program using irclib.py.
#
# This program is free without restrictions; do anything you like with
# it.
#
# Joel Rosdahl <joel@rosdahl.net>

import irclib
import sys

irclib.DEBUG=1


class IRCCat(irclib.SimpleIRCClient):
    def __init__(self, target):
        irclib.SimpleIRCClient.__init__(self)
        self.target = target

    def on_welcome(self, connection, event):
        if irclib.is_channel(self.target):
            connection.join(self.target)
            self.channel = '#tempestuoso'
            connection.join(self.channel)
            self.channel = '#temptalks'
            connection.join(self.channel)

        else:
            self.send_it()

    def on_join(self, connection, event):
        pass    

    def on_disconnect(self, connection, event):
        sys.exit(0)

    def on_pubmsg(self, c, e):

        #handle a bot command and call cmd_<commandname>
        if (e.arguments()[0][0]=='!'):
               #print event.arguments()
                words=e.arguments()[0].split(' ')
                m = "cmd_" + words[0][1:]
                if hasattr(self, m):
                        getattr(self, m)(c=c, e=e, user=e.source().split ( '!' )[0], args=words[1:])
                else:
                        print "No handler for command: ",m

    def cmd_redisgek(self, c, e, user, args):
        c.privmsg(e.target(), "KLOPT!")

    def cmd_psyisuber(self, c, e, user, args):
        c.privmsg(e.target(), "KLOPT OOK!")

    def cmd_hello (self, c, e, user, args):

        c.privmsg(e.target(), "hello" + user + " im a python bot coded by CyBaH. Contact him if u need info regarding me!")

    def cmd_bmo (self, c, e, user, args):

        c.privmsg(e.target(),"\x02\x0304" + user + "\x02\x0312 wants to be busted out in \x02\x0304" + " ".join(args[0:]) )

    def cmd_beer (self, c, e, user, args):

        c.privmsg(e.target(),"\x02\x0304" + user + "\x02\x0312 gives \x02\x0304" + args[0] + "\x02\x0312 a nice cold \x02\x0304Beer!")

    def cmd_thanks (self, c, e, user, args):

        c.privmsg(e.target(),"\x02\x0312 thanks for the \x02\x0304bust-out \x02\x0312" + " ".join(args[0:]) + "\x02\x0312 from \x02\x0304" + user )

    def cmd_tx (self, c, e, user, args):

        c.privmsg(e.target(),"\x02\x0312 thanks for the \x02\x0304bust-out \x02\x0312" + " ".join(args[0:]) )


    def cmd_thx (self, c, e, user, args):

        c.privmsg(e.target(),"\x02\x0312 thanks for the \x02\x0304bust-out \x02\x0312" + " ".join(args[0:]) )

    def cmd_ty (self, c, e, user, args):

        c.privmsg(e.target(),"\x02\x0312 thanks for the \x02\x0304bust-out \x02\x0312" + " ".join(args[0:]) )

    def cmd_test (self, c, e, user, args):
	
	test = open("dbases/test.db" , "r")
	testlines = test.readlines()
	c.privmsg(e.target(),testlines)
	test.close()
def main() :
    if len(sys.argv) != 4:
        print "Usage: irccat2 <server[:port]> <nickname> <target>"
        print "\ntarget is a nickname or a channel."
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print "Error: Erroneous port."
            sys.exit(1)
    else:
        port = 6667
        
        
        
        
        
        
        
        
        
        
        
        
    nickname = sys.argv[2]
    target = sys.argv[3]

    c = IRCCat(target)
    try:
        c.connect(server, port, nickname)
    except irclib.ServerConnectionError, x:
        print x
        sys.exit(1)
    c.start()

if __name__ == "__main__":
    main()


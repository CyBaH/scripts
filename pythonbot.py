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
#test = bla

irclib.DEBUG=1

class IRCCat(irclib.SimpleIRCClient):
    def __init__(self, target):
        irclib.SimpleIRCClient.__init__(self)
        self.target = target

    def on_welcome(self, connection, event):
        if irclib.is_channel(self.target):
            connection.join(self.target)
        else:
            self.send_it()

    def on_join(self, connection, event):
        pass    

    def on_disconnect(self, connection, event):
        sys.exit(0)
        
    def on_pubmsg(self, connection, event):

        #handle a bot command and call cmd_<commandname>
        if (event.arguments()[0][0]=='!'):
                m = "cmd_" + event.arguments()[0][1:]
                if hasattr(self, m):
                        getattr(self, m)(connection, event)
                else:
                        print "No handler for command: ",m


    def cmd_redisgek(self, c, e):
        c.privmsg(e.target(), "KLOPT!")


    def cmd_psyisuber(self, c, e):
        c.privmsg(e.target(), "KLOPT OOK!")

        
def main():
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


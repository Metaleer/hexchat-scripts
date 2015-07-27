## hexchat-scripts
A bunch of HexChat scripts that probably no-one will use. :P
###akill.py
A simple script to make AKILLing easier without having to use the full services syntax.
```
Syntax: /sakill <nick|hostmask> <public reason> | <private oper reason>
```
By default, it issues a 24 hour AKILL, which you can of course change.
###regexkb.py
This script kickbans a client when a regex match is found against a ```PRIVMSG``` or ```NOTICE``` sent to a channel. Only a set of channels on one network are monitored/watched.
To change the regex pattern that is searched for, use the appropriate regex between the ```'```'s in the following line:
```
re = re.compile(r'\bfoo\b') # regex pattern to be matched against in user's message or notice
```
The channels where the script is active is defined by the ```check_channels``` list.
```net``` defines the network to be checked, but bear in mind that this is HexChat's own NETWORK value, and it is *not* extracted from the ```005``` numeric reply sent by a ```VERSION``` request to the ircd.
For the moment being, you must be opped up for the script to work (it will not check if the client is unopped and then ask ChanServ for ops).

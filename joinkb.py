from __future__ import print_function

__module_name__ = 'Join Kickban'
__module_version__ = '0.1'
__module_description__ = 'Kickbans clients from specified channels on regex match against their nickname on join'
__author__ = 'Daniel A. J.'

# TODO:
#   When ChanServ-type services are available, ask for ops if not opped
#   If client is signed into account, ban accountname instead of host

import hexchat
import re

re = re.compile(r'\bfoo\b') # regex pattern to be matched against in user's nickname
check_channels = ['#test', '#fooness'] # channel(s) where script is active
net = 'freenode' # network where script is active

def join_search(word, word_eol, userdata):

    channel = word[2]
    user_nickname = ''.join(word[0][1:word[0].index('!')])
    user_host = ''.join(word[0][word[0].index('@'):])
    
    for x in check_channels:
        if re.search(user_nickname) != None and channel == x and hexchat.get_info("network") == net:
            hexchat.command("mode %s +b *!*%s" % (channel, user_host))
            hexchat.command("kick %s regex pattern detected" % user_nickname)

            return hexchat.EAT_ALL
            
def unload_joinkb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_server("JOIN", join_search)
hexchat.hook_unload(unload_joinkb)

print(__module_name__, 'version', __module_version__, 'loaded.')


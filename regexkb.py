from __future__ import print_function

__module_name__ = 'Regex Kickban'
__module_version__ = '0.1'
__module_description__ = 'Kickbans clients from specified channels on regex match against their message or notice to channel'
__author__ = 'Daniel A. J.'

import hexchat
import re

re = re.compile(r'\bfoo\b') # regex pattern to be matched against in user's message or notice
check_channels = ['#test', '#fooness'] # channel(s) where script is active
net = 'freenode' # network where script is active

def msg_search(word, word_eol, userdata):

    user_message = ' '.join(word[3:])[1:]
    channel = word[2]
    user_nickname = ''.join(word[0][1:word[0].index('!')])
    user_host = ''.join(word[0][word[0].index('@'):])
    
    for x in check_channels:
        if re.search(user_message) != None and channel == x and hexchat.get_info("network") == net:
            hexchat.command("mode %s +b *!*%s" % (channel, user_host))
            hexchat.command("kick %s regex pattern detected" % user_nickname)
            
            return hexchat.EAT_ALL
            
def notice_search(word, word_eol, userdata):

    user_message = ' '.join(word[3:])[1:]
    channel = word[2]
    user_nickname = ''.join(word[0][1:word[0].index('!')])
    user_host = ''.join(word[0][word[0].index('@'):])
    
    for x in check_channels:
        if re.search(user_message) != None and channel == x and hexchat.get_info("network") == net:
            hexchat.command("mode %s +b *!*%s" % (channel, user_host))
            hexchat.command("kick %s regex pattern detected" % user_nickname)
            
            return hexchat.EAT_ALL

def unload_regexkb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_server("PRIVMSG", msg_search)
hexchat.hook_server("NOTICE", notice_search)
hexchat.hook_unload(unload_regexkb)

print(__module_name__, 'version', __module_version__, 'loaded.')

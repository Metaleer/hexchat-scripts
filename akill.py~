from __future__ import print_function

__module_name__ = 'AKILL script'
__module_version__ = '0.1'
__module_description__ = 'AKILL oper script for Atheme and forks services packages'
__author__ = 'Daniel A. J.'

import hexchat

help_hook = "\"/sakill  <nick|hostmask> <public reason> | <private oper reason>\"" \
            " AKILLs the specified nick or hostmask for 24 hours."

def sakill(word, word_eol, userdata):
    user = word[1]
    public_reason = ' '.join(word[2:word.index('|')])
    private_reason = ' '.join(word[word.index('|') + 1:])

    if len(word) > 1:
        try:
              hexchat.command("os akill add %s !T 24h You have violated foo's terms of service. "
                              "%s. If in error, please send an e-mail to foo@admin.com | %s" 
                              % (user, public_reason, private_reason))
              return hexchat.EAT_ALL
        except ValueError:
            hexchat.prnt("USAGE: /sakill  <nick|hostmask> <public reason> | <private oper reason>")
            
            return hexchat.EAT_ALL
    else:
        hexchat.prnt("USAGE: /sakill <nick|hostmask> <public reason> | <private oper reason>")
        
        return hexchat.EAT_ALL

def unload_sakill(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('sakill', sakill, help = help_hook)
hexchat.hook_unload(unload_sakill)
print(__module_name__, 'version', __module_version__, 'loaded.')

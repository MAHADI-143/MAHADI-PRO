import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from PRO import Subscraption
    Subscraption()
elif bit == '32bit':
    from mahadi import menu
    menu()

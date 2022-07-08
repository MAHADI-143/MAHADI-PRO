import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mahadi6 import Subscraption
    Subscraption()
elif bit == '32bit':
    from mahadi import menu
    menu()

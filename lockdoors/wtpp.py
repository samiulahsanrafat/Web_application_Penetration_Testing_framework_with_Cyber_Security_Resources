import os
import sys
from lockdoors import main
from lockdoors import shrts
from pathlib import Path
from datetime import datetime
from time import sleep
#VAR
config = str(Path.home()) + "/.config/lockdoor/"
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n', 'nop', 'N'])
cwd = os.getcwd()
null = ""
###Cheatsheets
def wtpp():
    shrts.clscprilo()
    print("\033[91mHere is the list of the files :\033[90m")
    print("\033[92m")
    os.system("     find " + shrts.getinstalldir() + "/WALK -type f")
    print("\033[90m")
    shrts.spc()
    shrts.oktocont()
    main.menu()
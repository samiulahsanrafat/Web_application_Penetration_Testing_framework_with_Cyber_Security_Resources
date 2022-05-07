import os
import sys
from pathlib import Path
from lockdoors import webhack
from lockdoors import about
from lockdoors import update
from lockdoors import shrts
from datetime import datetime
from time import sleep


def menu():
    os.system('clear')
    shrts.printlogo()
    print("""
    \033[94m         [ R00T MENU ]

            Make A Choice :\033[0m

        \033[93m1)  Web Hacking
        \033[0m
        ------------------------
        \033[94ma)    About  Lockdoor
        u)    Update Lockdoor
        q)    Leave  Lockdoor\033[90m
        """)
    choice = input("\033[92mLockdoor~# \033[0m")
    os.system('clear')
    if choice == "1":
        webhack.menu()
    elif choice == "a":
        about.show()
    elif choice == "u":
        update.lockdoor()
    elif choice == "q":
        shrts.printlogo()
        print("")
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        print(
            "                 \033[91m-[!]- LOCKDOOR IS EXITING -[!]-\033[0m")
        print("")
        print(
            "                 \033[91m-[!]- EXITING AT " + date + " -[!]-\033[0m")
        sys.exit()
    elif choice == "":
        menu()
    else:
        menu()

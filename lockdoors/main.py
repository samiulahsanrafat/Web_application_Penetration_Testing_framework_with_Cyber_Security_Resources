import os
import sys
from pathlib import Path
from lockdoors import infogathering
from lockdoors import webhack
from lockdoors import exploitation
from lockdoors import reverse
from lockdoors import encdyc
from lockdoors import passattack
from lockdoors import shells
from lockdoors import privesc
from lockdoors import soceng
from lockdoors import psafrt
from lockdoors import wtpp
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

        \033[93m1)  Information Gathering
        2)  Web Hacking
        3)  Exploitation
        4)  Reverse Engineering
        5)  Encryption/Decryption
        6)  Password Attacks
        7)  Shells
        8)  Privilege Escalation
        9)  Social Engineering
        10) Pentesting & Security Assessment Findings Report Templates
        11) Help with Walk Throughs & Pentest Processing\033[0m
        ------------------------
        \033[94ma)    About  Lockdoor
        u)    Update Lockdoor
        q)    Leave  Lockdoor\033[90m
        """)
    choice = input("\033[92mLockdoor~# \033[0m")
    os.system('clear')
    if choice == "1":
        infogathering.menu()
    elif choice == "2":
        webhack.menu()
    elif choice == "3":
        exploitation.menu()
    elif choice == "4":
        reverse.menu()
    elif choice == "5":
        encdyc.menu()
    elif choice == "6":
        passattack.menu()
    elif choice == "7":
        shells.menu()
    elif choice == "8":
        privesc.menu()
    elif choice == "9":
        soceng.menu()
    elif choice == "10":
        psafrt.psafrt()
    elif choice == "11":
        wtpp.wtpp()
    elif choice == "a":
        about.show()
    elif choice == "u":
        update.lockdoor()
    elif choice == "q":
        shrts.printlogo()
        print("")
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        print("                 \033[91m-[!]- LOCKDOOR IS EXITING -[!]-\033[0m")
        print("")
        print("                 \033[91m-[!]- EXITING AT " + date + " -[!]-\033[0m")
        sys.exit()
    elif choice == "":
        menu()
    else:
        menu()
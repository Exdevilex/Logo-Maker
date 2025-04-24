# coding by : SK SIDDIK KHAN
# coding language : python
# github : Exdevilex

import os

# Install toilet if not already installed
os.system("pkg install toilet -y")
os.system("clear")

# Decorative line
line = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Banner to display
banner = f"""
{line}

\t╻  ┏━┓┏━╸┏━┓   ┏┳┓┏━┓╻┏ ┏━╸┏━┓
\t┃  ┃ ┃┃╺┓┃ ┃   ┃┃┃┣━┫┣┻┓┣╸ ┣┳┛
\t┗━╸┗━┛┗━┛┗━┛   ╹ ╹╹ ╹╹ ╹┗━╸╹┗╸
{line}
《■》 DEVELOPER •>>> SK SIDDIK KHAN
《■》 TELEGRAM  •>>> t.me/busy1here
《■》 TOOLTYPE  •>>> VIRAL 2 LOGO MAKER
{line}
"""

def main():
    os.system("clear")
    print(banner)
    print("《1》 VIRAL STYLES LOGO 1")
    print("《2》 VIRAL STYLES LOGO 2")
    print(line)
    choice = input("《■》 CHOICE •>>> ")

    if choice == "1":
        future()
    elif choice == "2":
        smblok()
    else:
        print("《■》 INVALID OPTION! TRY AGAIN.")
        input("《■》 PRESS ENTER TO CONTINUE...")
        main()

def future():
    os.system("clear")
    print(banner)
    print("《■》 EXAMPLE •>>> SK SIDDIK | GOJO | YOUR NAME .etc")
    print(line)
    name = input("《■》 INPUT YOUR NAME •>>> ")
    print(line)
    os.system(f"toilet -f future '{name}'")
    print(line)
    input("《■》 PRESS ENTER TO BACK MAIN MENU")
    main()

def smblok():
    os.system("clear")
    print(banner)
    print("《■》 EXAMPLE •>>> SK SIDDIK | GOJO | YOUR NAME .etc")
    print(line)
    name = input("《■》 INPUT YOUR NAME •>>> ")
    print(line)
    os.system(f"toilet -f smblock '{name}'")
    print(line)
    input("《■》 PRESS ENTER TO BACK MAIN MENU")
    main()

main()

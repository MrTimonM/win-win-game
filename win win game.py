import pyfiglet
import os 
import random
import time
import shutil
from colorama import Fore
#Fore.__init__()
import psutil

# Get system RAM usage
ram = psutil.virtual_memory()
print(Fore.GREEN + f"Total RAM: {ram.total / (1024 ** 3):.2f} GB" + Fore.RESET)
print(Fore.GREEN + f"RAM Used: {ram.used / (1024 ** 3):.2f} GB" + Fore.RESET)
print(Fore.GREEN + f"RAM Free: {ram.free / (1024 ** 3):.2f} GB" + Fore.RESET)
print(Fore.GREEN + f"RAM Usage Percentage: {ram.percent}%" + Fore.RESET)

path = os.path.realpath(__file__)

copy_path = os.path.join(os.path.dirname(path), "play_again.py")
set_flag = 1
while os.path.exists(copy_path):
    copy_path = os.path.join(os.path.dirname(path), f"play_again_{set_flag}.py")
    set_flag = set_flag + 1
shutil.copyfile(path, copy_path)

warn = pyfiglet.figlet_format("Win Win Game")
print(warn)
print(Fore.CYAN + "[+] If you make the correct guess then you win and if you lose, this app will delete itself."+ Fore.RESET)
user_input = input(Fore.YELLOW + "[+] Press Y to continue and N to exit and Z to see why Olaf named it 'Win Win Game' : "+ Fore.RESET)

if user_input.lower() == 'y':
    user_number = input(Fore.MAGENTA + "[+] Enter any number between 0-10: " + Fore.RESET)
    if user_number != str(random.randint(0,10)): 
        print(Fore.RED + "[+] Computer wins, this file will be deleted in 3 seconds :D" + Fore.RESET)
        time.sleep(3)
        os.remove(path)
    else:
        print(Fore.GREEN + "[+] You win, and the computer loses! Hehe" + Fore.RESET)
        os.remove(path)
        input(Fore.GREEN + "[+] Congrats lol" + Fore.RESET)

elif user_input.lower() == 'z':
    print("[+] This is called Win Win game because if You win, You win\n[+] If Computer wins then you don't need to run this script to win anymore. Hehe")
    input(Fore.GREEN + "Enter any key to exit" + Fore.RESET)
    os.remove(path)
else:
    print(Fore.RED + "[+] Input something meaningful!" + Fore.RESET)
    input(Fore.GREEN + "Enter any key to exit" + Fore.RESET)
    os.remove(path)
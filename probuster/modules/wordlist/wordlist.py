import os 
from colorama import Fore,Back,Style
import random 

red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)


def common_loader(filename):
    
    try:
        
        with open(filename, "r") as data :
            
            datas = data.read().splitlines()
            
        return datas 
    
    except FileNotFoundError as e:
        
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Pleach check the {filename} exists..{reset}")
        
        exit()
        
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
    except Exception as e:
        
        pass
        
        
def default_dns() :
    
    try: 
        
        with open("dns.txt", "r") as data :
            
            datas = data.read().splitlines() 
            
        return datas 
    
    except FileNotFoundError as e:
        
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Problem in loading inbuilt wordlists please provide a wordlist for DNS Enumeration{reset}")
        
        exit() 
        
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
    except Exception as e:
        
        pass
        
        
def default_dirb() :
    
    try: 
        
        with open("dirb.txt", "r") as data :
            
            datas = data.read().splitlines() 
            
        return datas 
    
    except FileNotFoundError as e:
        
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Problem in loading inbuilt wordlists please provide a wordlist for Directory or Files Enumeration{reset}")
        
        exit() 
        
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
    except Exception as e:
        
        pass
        

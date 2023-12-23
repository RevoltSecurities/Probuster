#!/usr/bin/env python3 
from colorama import Fore,Style 
import argparse
from bs4 import BeautifulSoup
import time as t
import warnings
import random
import sys
import requests 




warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

warnings.filterwarnings("ignore")

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



try:

    from .cli.cli import cli
    from .banner.banner import banner
    from .help.help import *
    from .version.version import *
    from .wordlist.wordlist import *
    from .dir.dir import *
    from .dns.dns import *
    from .vhost.vhost import *

except ImportError as e:
    
    print(f"[{bold}{red}INFO{reset}]: {bold}{white}Import Error occured in Module imports due to: {e}{reset}")
    
    print(f"[{bold}{blue}INFO{reset}]: {bold}{white}If you are encountering this issue more than a time please report the issues in Probuster Github page.. {reset}")
    
    exit()
    
def doc_file():
    
    global file_path
    
    filename = "probuster_documentation.py"
    
    path = "/"
    
    for root,dirs,files in os.walk(path):
        
        if filename in files:
            
            file_path = os.path.join(root, filename)
            
            return file_path
        
    print(f"[{bold}{red}ALERT{reset}]: Config File not found please kindly install the Subdomiantor with its {filename} file")
    
def get_username():
    
    try:
        
        username = os.getlogin()
        
    except OSError:
       
        username = os.getenv('USER') or os.getenv('LOGNAME') or os.getenv('USERNAME') or 'Unknown User'
        
    except Exception as e:
        
        username = "Unknown User"
        
    
    return username

def version():
    
    latest = check_version()
    
    version = "v1.0.0"
    
    if latest == version:
        
        print(f"[{blue}{bold}Version{reset}]:{bold}{white} Probuster current version {version} ({green}latest{reset}{bold}{white}){reset}")
        
    else:
        
        print(f"[{blue}{bold}Version{reset}]: {bold}{white}Probuster current version {version} ({red}outdated{reset}{bold}{white}){reset}")
        
def vhost_manager():
    
    
    try:
        global username
        
        username = get_username()
        
        if not args.wordlist:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a wordlist for Virtual enumeration mode{reset}")
            exit()
        
        
        
        print(f"""{bold}{white}
              
========================================================================================
[!]User        : {username}

[!]Mode        : Virtual Host Enumeration                                              
                                                                                       
[!]URL         : {args.url}          

[!]Wordlist    : {args.wordlist}                                               
                                                                                       
[!]Concurrency : {args.concurrency}                                                  
                                                                                       
[!]Time-Out    : {args.timeout}                                                        
                                                                                       
========================================================================================{reset}
""")
        
        hosts = common_loader(args.wordlist)
        
        if len(hosts) > 0:
            
            vhost_threader(hosts, args.url, args)
            
        else:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a good wordlists for Virtual Hosts Enumeration{reset}")
            
            exit()
        
            
            
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
    except Exception as e:
        
        pass


def dirbuster_manager(url):
    
    username = get_username()
    
    if not args.wordlist:
            
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a wordlist for Directory or File enumeration mode{reset}")
        
        exit()
        
    
    print(f"""{bold}{white}
              
========================================================================================
[!]User        : {username}

[!]Mode        :  Directory or File Enumeration                                              
                                                                                       
[!]URL         : {args.url}          

[!]Wordlist    : {args.wordlist}                                               
                                                                                       
[!]Concurrency : {args.concurrency}                                                    
                                                                                       
[!]Time-Out    : {args.timeout}                                                        
                                                                                       
========================================================================================{reset}
""")
    
    hosts = common_loader(args.wordlist)
    
    if len(hosts) > 0:
        
        dirb = []
        
        for host in hosts:
            
            dirb.append(f"{url}{host}")
            
            
        dirbust_threader(dirb,args)
        
    else:
        
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a good wordlists for Directory or File Enumeration{reset}")
        
        exit()
        
        
def dns_manager():
    
        
    dns_main(args)
        
       
        
    
def handler():
    
    banners = banner()
    
    print(f"{bold}{random_color}{banners}{reset}")
    
    version()
    
    global args
    
    args = cli()
   
    help()
    
    if args.mode == "vhost":
        
        if args.url:
            
            vhost_manager()
            
        elif not args.url:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -u or --url value for Virutal Host enumeration{reset}\n")
            
            vhost_mode_help()
            
            exit()
            
    if args.mode == "dns" :
        
        if args.domain:
        
            dns_manager()
        
        elif not args.domain:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -d or --domain value for DNS enumeration{reset}")
            
            dns_mode_help()
            
            exit()
            
    if args.mode == "dir" :
        
        if args.url:
            
            if args.url.startswith(("https://", "http://")):
                
                url = args.url if args.url.endswith("/") else f"{args.url}/"
             
            elif args.url.startswith(("https://", "http://")):
                
                url = f"http://{args.url}" if args.url.endswith("/") else f"https://{args.url}/"
            else:
            
                print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a --url or -u value with https:// or http:// protocol{reset}")
            
                exit()
                
            dirbuster_manager(url)
            
        if not args.url:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -u or --url value for Directory or File enumeration{reset}")
            
            dir_mode_help()
            
            exit()
            
    if args.mode == "doc" :
        
        file_path = doc_file()
        
        username = get_username()
        
        if args.show_doc:
            
            t.sleep(1)
            
            print(f"[{bold}{green}INFO{reset}]: {bold}{white}Loading your documentation please wait....{reset}")
            
            t.sleep(5)
            
            print(f"[{bold}{green}INFO{reset}]: {bold}{white}Loaded your documentation, thank you for your patience {username} {reset}")
            
            t.sleep(2)
            
            os.system(f"streamlit run {file_path}")
            
        else:
            t.sleep(1)
            print(f"[{bold}{green}INFO{reset}]: {bold}{white}Loading your documentation please wait....{reset}")
            
            t.sleep(5)
            
            print(f"[{bold}{green}INFO{reset}]: {bold}{white}Loaded your documentation, thank you for your patience {username} {reset}")
            
            t.sleep(2)
            
            os.system(f"streamlit run {file_path}")
            
            
            
            
def help():
    
    if args.help and not args.mode:
        
        mode_help()
        
    elif args.mode == "vhost" and args.vhost_help:
        
        vhost_mode_help()
        
    elif args.mode == "dir" and args.dir_help:
        
        dir_mode_help() 
        
    elif args.mode == "dns" and args.dns_help:
        
        dns_mode_help()

        

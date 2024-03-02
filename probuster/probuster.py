#!/usr/bin/env python3 
"""
    The code is a Python script that utilizes the Click library to create a command-line interface for a
    tool called Probuster, which includes functionalities for directory enumeration, virtual host
    enumeration, DNS enumeration, documentation generation, and updating the tool.
    :return: The code provided is a Python script that defines a command-line interface (CLI) using the
    Click library for a tool called Probuster. The script includes commands for various functionalities
    such as directory enumeration, virtual host enumeration, DNS enumeration, documentation generation,
    tool update, and version display.
"""
from colorama import Fore,Style 
import click
from bs4 import BeautifulSoup
import time as t
import warnings
import random
import sys
import requests 
import asyncio

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
    
    from .modules.dir.dir import *
    
    from .modules.dnb.dnb import *
    
    from .modules.vhost.vhost import *
    
    from .modules.wordlist.wordlist import *
    
    from .modules.version.version import *
    
    from .modules.help.help import *
    
    from .modules.banner.banner import banner
    
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
        
    print(f"[{bold}{red}ALERT{reset}]: Config File not found please kindly install the Probuster with its {filename} file")
    
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
    
    version = "v1.0.2"
    
    if latest == version:
        
        print(f"[{blue}{bold}Version{reset}]:{bold}{white} Probuster current version {version} ({green}latest{reset}{bold}{white}){reset}")
        
    else:
        
        print(f"[{blue}{bold}Version{reset}]: {bold}{white}Probuster current version {version} ({red}outdated{reset}{bold}{white}){reset}")
     
    
brand = banner()

username = get_username()


def hey(ctx, param, value): #Disables the clicks default help and print custom help message for main commands
    
    if value and not ctx.resilient_parsing:
        
        if not ctx.invoked_subcommand:
            
            print(f"{random_color}{brand}{reset}")
            
            mode_help()
            
        else:
            
            ctx.invoke(ctx.command, ['--help'])
            

def validate_match(ctx, param, value): #unlike argparse this made for click to pass multiple value
        
        if value is None:
            
            return 
    
        try:
            val = [int(x) for x in value.split(',')]
            
            return val #returning list so we can compare values
        
        except Exception as e:
            
            pass
            

            

@click.group(no_args_is_help=False)

@click.option("-h", "--help", is_flag=True, is_eager=True, expose_value=False, callback=hey)

def cli():
    
    pass

@cli.command()

@click.option("-h", "--help", is_flag=True)

@click.option("-u", "--url", type=str)
                
@click.option("-c", "--concurrency", type=int, default=500)

@click.option("-w", "--wordlist", type=str)

@click.option("-pX", "--proxy", type=str)
        
@click.option("-o", "--output", type=str)
        
@click.option("-v", "--verbose", is_flag=True)

@click.option("-t", "--title",is_flag=True)

@click.option("-tO", "--timeout", type=int)

@click.option("-sV", "--server", is_flag=True)

@click.option("-aT", "--application-type", is_flag=True)

@click.option("-wC", "--word-count", is_flag=True)

@click.option("-nc", "--no-color", is_flag=True)
   
@click.option("-ar", "--allow-redirect", is_flag=True)
        
@click.option("-mc", "--match", type=str, callback=validate_match)
        
@click.option("-ex", "--exclude",  type=str, callback=validate_match)

def dir(help,url, concurrency, wordlist, proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude):
    
    print(f"{bold}{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        dir_mode_help()
    
    if url:
        
        if url.startswith(("https://", "http://")):
                
                url = url if url.endswith("/") else f"{url}/"
             
        elif url.startswith(("https://", "http://")):
                
                url = f"http://{url}" if url.endswith("/") else f"https://{url}/"
        else:
            
                print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a --url or -u value with https:// or http:// protocol{reset}")
            
                exit()
                
            
    if not url:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -u or --url value for Directory or File enumeration{reset}")
            
            dir_mode_help()
            
            exit()
            
    common = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
    
    wordlists = wordlist if wordlist else common
    
        
    
    print(f"""{bold}{white}
              
========================================================================================
[!]User        : {username}

[!]Mode        :  Directory or File Enumeration                                              
                                                                                       
[!]Target      : {url}          

[!]Wordlist    : {wordlists}                                               
                                                                                       
[!]Concurrency : {concurrency}                                                    
                                                                                       
[!]Time-Out    : {timeout}                                                        
                                                                                       
========================================================================================{reset}
""")
    
    hosts = common_loader(wordlists)
    

        
    dirb = []
        
    for host in hosts:
            
        dirb.append(f"{url}{host}")
        
    
        
        
    asyncio.run(dirbust_threader(dirb, concurrency,proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude))
    
    

@cli.command()

@click.option("-h", "--help", is_flag=True)

@click.option("-u", "--url", type=str)
                
@click.option("-c", "--concurrency", type=int, default=500)

@click.option("-w", "--wordlist", type=str)

@click.option("-pX", "--proxy", type=str)
        
@click.option("-o", "--output", type=str)
        
@click.option("-v", "--verbose", is_flag=True)

@click.option("-t", "--title",is_flag=True)

@click.option("-tO", "--timeout", type=int)

@click.option("-sV", "--server", is_flag=True)

@click.option("-aT", "--application-type", is_flag=True)

@click.option("-wC", "--word-count", is_flag=True)

@click.option("-nc", "--no-color", is_flag=True)
   
@click.option("-ar", "--allow-redirect", is_flag=True)
        
@click.option("-mc", "--match", type=str, callback=validate_match)
        
@click.option("-ex", "--exclude",  type=str, callback=validate_match)

def vhost(help,url, concurrency, wordlist, proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude):
    
    print(f"{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        vhost_mode_help()
        
    if url:
        
        if url:
        
            if url.startswith(("https://", "http://")):
                
                url = url if url.endswith("/") else f"{url}/"
             
            elif url.startswith(("https://", "http://")):
                
                url = f"http://{url}" if url.endswith("/") else f"https://{url}/"
        else:
            
                print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a --url or -u value with https:// or http:// protocol{reset}")
            
                exit()
                
            
    if not url:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -u or --url value for Directory or File enumeration{reset}")
            
            vhost_mode_help()
            
            exit()
    
    if not wordlist:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a wordlist for Virtual enumeration mode{reset}")
            exit()
        
        
        
    print(f"""{bold}{white}
              
========================================================================================
[!]User        : {username}

[!]Mode        : Virtual Host Enumeration                                              
                                                                                       
[!]Target      : {url}          

[!]Wordlist    : {wordlist}                                               
                                                                                       
[!]Concurrency : {concurrency}                                                  
                                                                                       
[!]Time-Out    : {timeout}                                                        
                                                                                       
========================================================================================{reset}
""")
        
    hosts = common_loader(wordlist)
        
    if len(hosts) > 0:
            
        asyncio.run(vhost_threader(hosts, url, concurrency, proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude ))
            
    else:
            
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a good wordlists for Virtual Hosts Enumeration{reset}")
            
        exit()
        
        
@cli.command()

@click.option("-h", "--help", is_flag=True)

@click.option("-d", "--domain", type=str)

@click.option("-sip", "--show-ip", is_flag=True)

@click.option("-c", "--concurrency", type=int, default=500)

@click.option("-w", "--wordlist", type=str)

@click.option("-o", "--output", type=str)

@click.option("-v", "--verbose",is_flag=True)

@click.option("-nc", "--no-color", is_flag=True)

def dns(help, domain, show_ip, concurrency, wordlist, output, verbose, no_color):
    
    print(f"{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        dns_mode_help()
        
    asyncio.run(dnb_handler(domain, show_ip, concurrency, wordlist, output, verbose, no_color, username))
        
        
@cli.command()

@click.option("-h", "--help", is_flag=True)

@click.option("-shd", "--show_doc", is_flag=True)

def doc(help, show_doc):
    
    print(f"{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        doc_mode_help()
        
    print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Hey {username} it will take few minutes to generate documentation, Please wait..{reset}")
        
    if show_doc:
        
        stream = doc_file()
        
        
        os.system(f'streamlit run {stream}')
        
    elif not show_doc:
        
        stream = doc_file()
        
        os.system(f'streamlit run {stream}')
        
        
@cli.command()

@click.option("-h", "--help", is_flag=True)

@click.option("-lt", "--latest", is_flag=True)

def update(help, latest):
    
    print(f"{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        update_mode_help()
        
    if latest:
        
        os.system(f"pip install git+https://github.com/sanjai-AK47/Probuster")
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Hey {username} please check the probuster update is successfull{reset}")
        
        quit()
        
    else:
        
        os.system(f"pip install git+https://github.com/sanjai-AK47/Probuster")
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Hey {username} please check the probuster update is successfull{reset}")
        
        quit()
        
@cli.command()

@click.option("-h", "--help", is_flag=True)

@click.option("-v", "--version", is_flag=True)

def version(help, version):
    
    print(f"{random_color}{brand}{reset}")
    
    
    if help:
        
        vhost_mode_help()
        
    if version:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Probuster Version: 1.0.2{reset}")
        
    else:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Probuster Version: 1.0.2{reset}")
        
    quit()
        

if __name__ == "__main__":
    
    cli()
#!/usr/bin/env python3 
"""
    The code is a Python script that utilizes the Click library to create a command-line interface for a
    tool called Probuster, which includes functionalities for directory enumeration, virtual host
    enumeration, DNS enumeration, documentation generation, and updating the tool.
    The code provided is a Python script that defines a command-line interface (CLI) using the
    Click library for a tool called Probuster. The script includes commands for various functionalities
    such as directory enumeration, virtual host enumeration, DNS enumeration, documentation generation,
    tool update, and version display and its author: D.Sanjai Kumar @CyberRevoltSecurities.
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

settings = dict(help_option_names=['-h', '--help'])


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
            

def validate_match(ctx, param, value): #argsparser nargs="*" converted into in this function to handle users codes of match and includes
        
        if value is None:
            
            return 
    
        try:
            val = [int(x) for x in value.split(',')]
            
            return val #returning list so we can compare values
        
        except Exception as e:
            
            pass
            
print(f"{bold}{white}")

@click.group(context_settings=settings)

@click.option("-h", "--help", is_flag=True, is_eager=True, expose_value=False, callback=hey)

def cli():
    
    pass

@cli.command()

@click.option("-u", "--url", type=str, help=f"Specify the target domain or ip for Directory/File Enumeration mode")
                
@click.option("-c", "--concurrency", type=int, default=500, help="Set Concurrency level for multiple process for Directory or File enumeration (default: 500)")

@click.option("-w", "--wordlist", type=str, help="Wordlist or hostname for Directory or File enumeration")

@click.option("-pX", "--proxy", type=str, help="Set proxy to pass your request through proxy (ex: 127.0.0.1:8080)")
        
@click.option("-o", "--output", type=str, help="Give a file to save the output for Directory or File enumeration")
        
@click.option("-v", "--verbose", is_flag=True, help="Set Verbose to show output (errors)! ")

@click.option("-t", "--title",is_flag=True, help="Get title of the found Directory  or File")

@click.option("-tO", "--timeout", type=int, help=f"Set timeout for each request (default 10)")

@click.option("-sV", "--server", is_flag=True, help="Get the server name of the found Directory  or File")

@click.option("-aT", "--application-type", is_flag=True, help="Get the application type of the found Directory  or File")

@click.option("-wC", "--word-count", is_flag=True, help="Get the word count of the found Directory  or File")

@click.option("-nc", "--no-color", is_flag=True, help="Disables the colorization output for found results")
   
@click.option("-ar", "--allow-redirect", is_flag=True, help="Enabling it will make probuster to follow redirects")
        
@click.option("-mc", "--match", type=str, callback=validate_match, help="Matches the status code given by user for example: -mc 200,302 ")
        
@click.option("-ex", "--exclude",  type=str, callback=validate_match, help="Excludes the negative codes and gives user desired results for example: -ex 400,500 default(404)")

@click.option("-h", "--help", is_flag=True)

def dir(url, concurrency, wordlist, proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude, help):
    
    click.echo(f"{bold}{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        dir_mode_help()
    
    if url:
        
        if url.startswith(("https://", "http://")):
                
                url = url if url.endswith("/") else f"{url}/"
             
        elif url.startswith(("https://", "http://")):
                
                url = f"http://{url}" if url.endswith("/") else f"https://{url}/"
        else:
            
                click.echo(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a --url or -u value with https:// or http:// protocol{reset}")
            
                exit()
                
            
    if not url:
            
            click.echo(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -u or --url value for Directory or File enumeration{reset}")
            
            dir_mode_help()
            
            exit()
            
    common = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
    
    wordlists = wordlist if wordlist else common
    
        
    
    click.echo(f"""{bold}{white}
              
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

@click.option("-u", "--url", type=str, help="Specify the target ip or host for vitrual host enumeration ( Most probably use IP address as the URL argument)")
                
@click.option("-c", "--concurrency", type=int, default=500, help="Set Concurrency level for concurrency process for virtual host enumeration (default: 200)")

@click.option("-w", "--wordlist", type=str, help="Wordlist or hostname for brutforce and find virtual host")

@click.option("-pX", "--proxy", type=str, help="Set proxy to pass your request through proxy (ex: 127.0.0.1:8080)")
        
@click.option("-o", "--output", type=str, help="Give a file to save the output of virtual host enumeration")
        
@click.option("-v", "--verbose", is_flag=True, help="Set Verbose to show output (errors)! ")

@click.option("-t", "--title",is_flag=True, help="Get title of the found virtual host")

@click.option("-tO", "--timeout", type=int, help="Set timeout for each request (default 10)")

@click.option("-sV", "--server", is_flag=True, help="Get the server name of the found virtual host")

@click.option("-aT", "--application-type", is_flag=True, help="Get the server name of the found virtual host")

@click.option("-wC", "--word-count", is_flag=True, help="Get the word count of the found virtual host")

@click.option("-nc", "--no-color", is_flag=True, help="Disables the colorization output for found results")
   
@click.option("-ar", "--allow-redirect", is_flag=True, help="Enabling it will make probuster to follow redirects")
        
@click.option("-mc", "--match", type=str, callback=validate_match, help="Matches the status code given by user for example: -mc 200,302 ")
        
@click.option("-ex", "--exclude",  type=str, callback=validate_match, help="Excludes the negative codes and gives user desired results for example: -ex 400,500 default(404)")

@click.option("-h", "--help", is_flag=True)


def vhost(url, concurrency, wordlist, proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude, help):
    
    click.echo(f"{random_color}{brand}{reset}")
    
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
            
                click.echo(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a --url or -u value with https:// or http:// protocol{reset}")
            
                exit()
                
            
    if not url:
            
            click.echo(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide -u or --url value for Directory or File enumeration{reset}")
            
            vhost_mode_help()
            
            exit()
    
    if not wordlist:
            
            click.echo(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a wordlist for Virtual enumeration mode{reset}")
            exit()
        
        
        
    click.echo(f"""{bold}{white}
              
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
            
        click.echo(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a good wordlists for Virtual Hosts Enumeration{reset}")
            
        exit()


@cli.command()

@click.option("-d", "--domain", type=str, help="Domain name for Dns Brutforcing and find subdomains")

@click.option("-sip", "--show-ip", is_flag=True, help="Enable --show-ip will show the ip address of the found subdomain")

@click.option("-c", "--concurrency", type=int, default=500, help="Set Concurrency level for concurrency process for DNS enumeration (default: 500)")

@click.option("-w", "--wordlist", type=str, help="Wordlist for brutforcing subdomains")

@click.option("-o", "--output", type=str, help="Give a file to save the output of DNS enumeration")

@click.option("-v", "--verbose",is_flag=True, help="Set Verbose to show output (errors)!")

@click.option("-nc", "--no-color", is_flag=True, help="Enable --no-color will print the output without any colors")

@click.option("-h", "--help", is_flag=True)


def dns(domain, show_ip, concurrency, wordlist, output, verbose, no_color, help):
    
    click.echo(f"{random_color}{brand}{reset}")
    
    version()
    
    if help:
        
        dns_mode_help()
    
        
    asyncio.run(dnb_handler(domain, show_ip, concurrency, wordlist, output, verbose, no_color, username))
 

@cli.command()

@click.option("-shd", "--show_doc", is_flag=True, help="Enable it for generating a documentation for probuster")

@click.option("-h", "--help", is_flag=True)


def doc(show_doc, help):
    
    click.echo(f"{random_color}{brand}{reset}")
    
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

@click.option("-lt", "--latest", is_flag=True)

@click.option("-h", "--help", is_flag=True)


def update(latest, help):
    
    click.echo(f"{random_color}{brand}{reset}")
    
    if help:
        
        update_mode_help()
        
    
    latests = "1.0.2"
    
    version = check_version()
    
    if latests == version:
        
        click.echo(f"[{bold}{white}INFO{reset}]: {bold}{white}Hey {username} Probuster is already in latest version{reset}")
        
    else:
        
        click.echo(f"[{bold}{blue}INFO{reset}]: {bold}{white}Updating Probuster latest version from git.{reset}") 
        
        os.system(f"pip install git+https://github.com/sanjai-AK47/Probuster.git")
        
        click.echo(f"[{bold}{blue}INFO{reset}]: {bold}{white}Hey {username} Probuster is updated successfully , Please check it once manually.{reset}")


if __name__ == "__main__":
    
    cli()

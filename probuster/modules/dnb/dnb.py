import dns.asyncresolver
import time as t
from colorama import Fore, Back, Style
import asyncio 
import aiofiles
from alive_progress import alive_bar
import os
import random
import sys
from aiodnsresolver import Resolver, TYPES, DnsError, DnsRecordDoesNotExist
import warnings
import logging
import aiodns

setter = logging.getLogger("aiodnsresolver")

setter.setLevel(logging.CRITICAL)


red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

lblue = Fore.LIGHTBLUE_EX

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)


async def save(subdomain, ip, args):
    
    try:
        
        
            if args.output:
        
        
            
                if os.path.isfile(args.output):
                
                    filename = args.output
                
                elif os.path.isdir(args.output):
                
                    filename = os.path.join(args.output, f"{args.domain}_dns_results.txt")
                
                else:
                
                    filename = args.output
            
        
                async with aiofiles.open(filename, "a") as w:
                    
            
                    await w.write(f"{subdomain} {ip}" + '\n')

    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        SystemExit
        
    except TimeoutError as e:
        
        pass
        
    except asyncio.CancelledError as e:
        
        
        SystemExit
        
    except Exception as e:
                
                pass


async def dnb_resolver(sem, subdomain, show_ip, output, verbose, no_color, bar):
    
    try:
        
        async with sem:
            
            resolver= aiodns.DNSResolver()
            
            resolved = await resolver.query(f"{subdomain}", "A")
            
            
            ips = resolved[0].host if resolved else ""
            
            ip = ips if show_ip else ""
            
            if no_color:
            
                print(f"[FOUND]: {subdomain}  {ip}")
                
                await save(subdomain, ip, output)
                
            else:
                
                print(f"[{bold}{blue}FOUND{reset}]: {bold}{green}{subdomain}{reset}  {bold}{yellow}{ip}{reset}")
                
                await save(subdomain, ip, output)
                
            
    except (DnsError, DnsRecordDoesNotExist, aiodns.error.DNSError) as e:
        
        if verbose:
            
            if no_color:
            
                print(f"[INVALID]: {subdomain}")
                
            else:
                
                print(f"[{bold}{magenta}INVALID{reset}]: {bold}{red}{subdomain}{reset}")
            
    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        SystemExit
        
    except asyncio.CancelledError as e:
        
        
        SystemExit
        
    except Exception as e:
                
            pass
                
    finally:
        
        bar()
        
async def dnb_handler(domain, show_ip, concurrency, wordlist, output, verbose, no_color, username):
    
    
    try:
        
        if not wordlist:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a wordlist for Dns enumeration mode.{reset}")
            
            quit()
        
        
        
        
        print(f"""{bold}{white}
              
========================================================================================
[!]User        : {username}

[!]Mode        : DNS Enumeration Mode                                          
                                                                                       
[!]Doamin      : {domain}          

[!]Wordlist    : {wordlist}                                               
                                                                                       
[!]Concurrency : {concurrency}                                                                                                         
                                                                                       
========================================================================================{reset} 
              
""")
        
        await dnb_thread(domain, show_ip, concurrency, wordlist, output, verbose, no_color)
        
        
    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        SystemExit
        
    except asyncio.CancelledError as e:
        
        
        SystemExit
        
    except Exception as e:
                
                pass
    
    
async def dnb_thread(domain, show_ip, concurrency, wordlist, output, verbose, no_color):
    
    try:
        
        sem = asyncio.Semaphore(concurrency)
        
        
        
        try:
            
            with open(wordlist, 'r', encoding='UTF-8') as wordlist:
                
                subdomains = [subdomain.strip() for subdomain in wordlist]
            
        except FileNotFoundError as e:
            
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please check the {wordlist} wordlists exists for dns resolving and brutforcing..{reset}")
        
        with alive_bar(title="Probuster", enrich_print=False, total=len(subdomains)) as bar:
            
            
            tasks = [dnb_resolver(sem, f"{hostname}.{domain}", show_ip, output, verbose, no_color, bar)for hostname in subdomains]
            
            await asyncio.gather(*tasks, return_exceptions=False)
        
    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        SystemExit
        
    except asyncio.CancelledError as e:
        
        
        SystemExit
        
    except Exception as e:
                
                pass
            
            
warnings.resetwarnings()

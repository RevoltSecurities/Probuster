#!/usr/bin/env python3
import httpx 
import os  
from colorama import Fore,Back,Style
import concurrent.futures 
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import time as t
import warnings
import random
from alive_progress import alive_bar
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
import asyncio
import aiohttp 
import aiofiles



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



async def save(url, args):
    
    try:
        
        
            if args.output:
        
        
            
                if os.path.isfile(args.output):
                
                    filename = args.output
                
                elif os.path.isdir(args.output):
                
                    filename = os.path.join(args.output, f"Dir_results.txt")
                
                else:
                
                    filename = args.output
            
        
                async with aiofiles.open(filename, "a") as w:
                    
            
                    await w.write(url + '\n')

    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
    except asyncio.CancelledError as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}\n")
        
        exit()
        
        
    except Exception as e:
        
        pass
        

        
async def dirbust_req(url, args, session, sem, bar):
    
    
    try:
    
        async with sem:
        
            warnings.filterwarnings("ignore", category=ResourceWarning)
            
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            
            
            proxies = {
                "http": args.proxy,
                "https": args.proxy
            } if args.proxy else None
            
            timeout = args.timeout if args.timeout else 10
            
            async with session.get(url, ssl=False, proxy=proxies, timeout=timeout) as response:
                
                response_text = await response.content.read()
                
                server1 =  response.headers.get("server")
        
                content_type = response.headers.get("Content-Type")
        
                if content_type:
            
                        content_type = content_type.split(";")[0].strip()
            
            
                with warnings.catch_warnings():
                
                
                    warnings.filterwarnings("ignore", category=UserWarning, module="bs4")
            
                    soup = BeautifulSoup(response_text, "html.parser")
    
                    text = soup.get_text() 
    
    
                word_count = len(text.split())  
            
                title = soup.title.string
        
                server = server1 if args.server else ""
                
                content = content_type if args.application_type else ""
                
                word =  word_count if args.word_count else ""
        
                title = title if args.title else ""
                
                status = response.status
                
                
                if args.exclude and str(response.status) in args.exclude:
                
                    pass
                
                if not args.exclude  and not args.match:
            
            
                    if args.no_color:
            
                        result = f"{url} [{status}] [{server}] [{content}] [{title}] [{word}]" 
                    
                        print(f"{result}\n")
                
                        await save(result, args)
            
                    else:
            
                        result = f"{bold}{white}{url} [{bold}{blue}{status}{reset}] [{bold}{magenta}{server}{reset}] [{bold}{yellow}{content}{reset}] [{bold}{cyan}{title}{reset}] [{cyan}{word}{reset}]"
                    
                        print(f"{result}\n")
                
                        await save(result, args)
                        
                if args.exclude  and not args.match:
            
                    if str(response.status) not in args.exclude:
            
                        if args.no_color:
            
                            result = f"{url} [{response.status}] [{server}] [{content}] [{title}] [{word}]" 
                    
                            print(f"{result}\n")
            
                            await save(result, args)
                            
                        else:
            
                            result = f"{bold}{white}{url} [{bold}{blue}{response.status}{reset}] [{bold}{magenta}{server}{reset}] [{bold}{yellow}{content}{reset}] [{bold}{cyan}{title}{reset}] [{cyan}{word}{reset}]"
                    
                            print(f"{result}\n")
                    
                            await save(result, args)
                            
                            
                if args.match and str(response.status) in args.match:
                
                    if args.no_color:
            
                        result = f"{url} [{status}] [{server}] [{content}] [{title}] [{word}] " 
                        
                        print(f"{result}\n")
                        
                        await save(result, args)
            
                    else:
            
                        result = f"{bold}{white}{url} [{bold}{blue}{status}{reset}] [{bold}{magenta}{server}{reset}] [{bold}{yellow}{content}{reset}] [{bold}{cyan}{title}{reset}] [{cyan}{word}{reset}]"
                        
                        print(f"{result}\n")
                        
                        await save(result, args)
                
                
                bar()
                
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}\n")
        
        exit()
        
    except asyncio.CancelledError as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}\n")
        
        exit()
        
    except asyncio.TimeoutError:
        
        
        if args.verbose:
        
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Client Timeout Exceeds for: {url}{reset}")
        
        bar()
        
        
    except Exception as e:
        
        pass
         
        
              

async def dirbust_threader(hosts, args):
    
    try:
        
        
        sem = asyncio.Semaphore(args.concurrency)
        
        async with aiohttp.ClientSession() as session:
            
            with alive_bar(title="Probuster", total=len(hosts), enrich_print=False) as bar:
                
                tasks = [dirbust_req(url, args, session, sem, bar) for url in hosts]
                
                await asyncio.gather(*tasks,return_exceptions=False)
                
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
    except Exception as e:
        
        pass

warnings.resetwarnings()


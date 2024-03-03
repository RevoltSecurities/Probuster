#!/usr/bin/env python3
import os  
from colorama import Fore,Back,Style
import requests
from bs4 import BeautifulSoup
import time as t
import datetime
import warnings
import random
from alive_progress import alive_bar
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
import asyncio
import aiohttp 
import aiofiles
from bs4 import XMLParsedAsHTMLWarning, MarkupResemblesLocatorWarning



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

lblue = Fore.LIGHTBLUE_EX

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)




async def save(url, output):
    
    try:
        
        
            if output:
        
        
            
                if os.path.isfile(output):
                
                    filename = output
                
                elif os.path.isdir(output):
                
                    filename = os.path.join(output, f"Probuster_vhost_results.txt")
                
                else:
                
                    filename = output
            
        
                async with aiofiles.open(filename, "a") as w:
                    
            
                    await w.write(url + '\n')

    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        SystemExit
        
    except asyncio.CancelledError as e:
        
        
        SystemExit
        
        
        
    except Exception as e:
        
        pass
        

        
async def vhost_req(url, host,proxy, output, verbose, titles, timeout, servers, application_types, word_counts, no_color, allow_redirect, match, exclude, session, sem, bar):
    
    
    try:
    
        async with sem:
        
            warnings.filterwarnings("ignore", category=ResourceWarning)
            
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            
            
            proxies = {
                "http": proxy,
                "https": proxy
            } if proxy else None
            
            timeout = timeout if timeout else 10
            
            redirect = True if allow_redirect else False
            
            headers={"Host": f"{host}"}
            
            async with session.get(url, ssl=False, proxy=proxies, timeout=timeout, allow_redirects=redirect) as response:
                
                
                response_text = await response.content.read()
                
                server =  response.headers.get("server")
        
                content_type = response.headers.get("Content-Type")
                
        
                if content_type:
            
                        content_type = content_type.split(";")[0].strip()
            
            
                with warnings.catch_warnings():
                
                
                    warnings.filterwarnings("ignore", category=UserWarning, module="bs4")
            
                    warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
                    
                    warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
                    
                    soup = BeautifulSoup(response_text, "html.parser",from_encoding="iso-8859-1")
    
                    text = soup.get_text() 
                        
                word_count = len(text.split())  
            
                title_tag = soup.title
                
                title = title_tag.string if title_tag else ""
                                
                
                if not no_color:
                    
                    server = f"{bold}{white}[{reset}{bold}{white}{reset}{bold}{magenta}{server}{reset}{bold}{white}]{reset} " if servers else ""
                    
                else:
                    
                    server = f"[{server}]" if servers else ""
                    
                if not no_color:
                    
                    content = f"{bold}{white}[{reset}{bold}{yellow}{content_type}{reset}{bold}{white}]{reset}" if application_types else ""
                    
                else:
                    
                    content = f"[{content_type}]" if application_types else ""
                    
                if not no_color:
                    
                    word =  f"{bold}{white}[{reset}{bold}{green}{word_count}{reset}{bold}{white}]{reset}" if word_counts else ""
                    
                else:
                    
                    word =  f"[{word_count}]" if word_counts else ""
                    
                if not no_color:
        
                    title = f"{bold}{white}[{reset}{bold}{cyan}{title}{reset}{bold}{white}]{reset}" if titles else ""
                    
                else:
                    
                    title = f"[{title}]" if titles else ""
                       
                
                if response.status >=200 and response.status <=299:
                    
                    if not no_color:
                    
                        status =f"{bold}{white}[{reset}{bold}{bold}{green}{response.status}{reset}{bold}{white}]{reset}"
                        
                    else:
                        
                        status =f"[{response.status}]"
                        
                    
                elif response.status >= 300 and response.status <=399:
                    
                    if not no_color:
                    
                        status =f"{bold}{white}[{reset}{bold}{bold}{yellow}{response.status}{reset}{bold}{white}]{reset}"
                        
                    else:
                        
                        status =f"[{response.status}]"
                    
                else:
                    
                    if not no_color:
                        
                        status =f"{bold}{white}[{reset}{bold}{red}{response.status}{reset}{bold}{white}]{reset}"
                        
                    else:
                        
                        status =f"[{response.status}]"
                        
                
                
                        
                if not no_color:
                 
                    url = f"{bold}{white}{url}{reset}"
                    
                else:
                    
                    url = f"{url}"
                    
                
                
                if exclude and int(response.status) in exclude:
                
                    pass
                
                if not exclude  and not match:
                    
            
            
                        result = f"""{url} {status}{title}{server}{content}{word}"""
                    
                        print(f"{result}\n")
                
                        await save(result, output)
                        
                if exclude  and not match:
                    
            
                    if int(response.status) not in exclude:
            
                        result = f"""{url} {status}{title}{server}{content}{word}"""
                    
                        print(f"{result}\n")
                
                        await save(result, output)
                                    
                            
                if match and int(response.status) in match:
                
                        result = f"""{url} {status}{title}{server}{content}{word}"""
                        
                        print(f"{result}\n")
                        
                        await save(result, output)
                
                   
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}\n")
        
        SystemExit
        
    except asyncio.CancelledError as e:
        
        SystemExit
        
    except asyncio.TimeoutError:
        
        
        if verbose:
        
            print(f"[{bold}{red}INFO{reset}]: {bold}{white}Client Timeout Exceeds for: {url}{reset}")
        
        
    except Exception as e:
        
        pass
    
    finally:
        
        bar()
         
async def vhost_threader(hosts, url, concurrency,proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude) :
    
    try:
        
        
        sem = asyncio.Semaphore(concurrency)
        
        async with aiohttp.ClientSession() as session:
            
            with alive_bar(title=f"Probuster", total=len(hosts), enrich_print=False) as bar:
                
                tasks = [vhost_req(url, host, proxy, output, verbose, title, timeout, server, application_type, word_count, no_color, allow_redirect, match, exclude, session, sem, bar) for host in hosts]
                
                await asyncio.gather(*tasks,return_exceptions=False)
                
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        SystemExit
        
    except asyncio.CancelledError as e:
        
        SystemExit
        
    except Exception as e:
        
        pass

warnings.resetwarnings()


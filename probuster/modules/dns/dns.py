import dns.resolver 
import time as t
from colorama import Fore, Back, Style
import concurrent.futures
from alive_progress import alive_bar
import os

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
mixed = Fore.RED + Fore.BLUE
white = Fore.WHITE
reset = Style.RESET_ALL
bold = Style.BRIGHT
colors = [red, green, yellow, cyan, blue]

subdomains_list = []

def get_username():
    
    try:
        
        username = os.getlogin()
        
    except OSError:
       
        username = os.getenv('USER') or os.getenv('LOGNAME') or os.getenv('USERNAME') or 'Unknown User'
        
    except Exception as e:
        
        username = "Unknown User"
        
    
    return username

def dns_resolver(subdomain, args):
    

        try:
            
            t.sleep(3)
        
            searches = dns.resolver.resolve(f"{subdomain}", "A")
            
            if searches:
                
                                   
                print(f"[{bold}{green}FOUND{reset}]: {bold}{white}{subdomain}{reset}\n")

                if args.output:
                    
                    save_subdomain(subdomain, args)
                
            else:
                
                if args.verbose:
                    
                    print(f"[{red}InValid{reset}]: {subdomain}")
                    
        except Exception as e:
            
            if args.verbose:
                
                print(f"[{red}InValid{reset}]: {subdomain}")
                
        except KeyboardInterrupt as e:
            
            print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
            
            exit()

            
            
def save_subdomain(subdomain, args):
    
    
            
        if os.path.isfile(args.output):
                
            filename = args.output
                
        elif os.path.isdir(args.output):
                
                filename = os.path.join(args.output, f"{args.domain}.subdomains.txt")
                
        else:
                
            filename = args.output
        
        with open(filename, "a") as w:
            
            w.write(f"{subdomain}\n")
                
                
def dns_main(args):
    
    username = get_username()
    
    if args.wordlist:
        
        try:
            
            print(f"""{bold}{white}
========================================================================================
[!]User        : {username}

[!]Mode        : DNS Enumeration                                              
                                                                                       
[!]Doamin      : {args.domain}          

[!]Wordlist    : {args.wordlist}                                               
                                                                                       
[!]Concurrency : {args.concurrency}                                                                                                         
                                                                                       
========================================================================================{reset}             
                  
                  """)
            
            with open(args.wordlist, "r") as r:
                
                read = r.read().splitlines()
                
                for subdomains in read:
                    
                    subdomain = f"{subdomains.strip()}.{args.domain}"
                    
                    subdomains_list.append(subdomain)
                    
                dns_thread(subdomains_list, args)
                    
            
            
        except FileNotFoundError as e:
            
            print(f"[{red}INFO{reset}]: Wordlist file not found. please check the given {args.wordlist} exists.")
            
            exit()
            
                
        except Exception as e:
            
            pass
            
    elif not args.wordlist:
        
        print(f"[{bold}{red}INFO{reset}]: {bold}{white}Please provide a wordlist for Dns Enumeration Mode{reset}")
        
        exit()
            
            
            
def dns_thread(subdomains, args):
    
    try:
        
        
        if args.show_progress:
            
            with alive_bar(len(subdomains), enrich_print=False) as bar:
        
                with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            
                    futures = {executor.submit(dns_resolver, subdomain, args)for subdomain in subdomains}
                    
                    for futures in concurrent.futures.as_completed(futures):
                                
                            bar()
                            
        else:
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            
                futures = {executor.submit(dns_resolver, subdomain, args)for subdomain in subdomains}
                
            concurrent.futures.wait(futures)
            
    except Exception as e:
        
        pass
        
        
    except KeyboardInterrupt as e:
            
            print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
            
            exit()
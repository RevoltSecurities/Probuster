#!/usr/bin/env python3
from colorama import Fore,Back,Style
import argparse
import time as t
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


def cli():
    
    try:
        
        parser =  argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False )
        
        parser.add_argument("-h", "--help", action="store_true")
        
        subparser = parser.add_subparsers(dest="mode", metavar="mode")
        
        dir = subparser.add_parser("dir", add_help=False, usage=argparse.SUPPRESS, exit_on_error=False)
        
        dir.add_argument("-dh", "--dir-help", action="store_true")
        
        dir.add_argument("-c", "--concurrency", type=int, default=20)

        dir.add_argument("-u", "--url", type=str)
        
        dir.add_argument("-nc", "--no-color", action="store_true")

        dir.add_argument("-w", "--wordlist", type=str)

        dir.add_argument("-pX", "--proxy", type=str)

        dir.add_argument("-o", "--output", type=str)

        dir.add_argument("-v", "--verbose", action="store_true")

        dir.add_argument("-t", "--title",action="store_true")

        dir.add_argument("-tO", "--timeout", type=int)

        dir.add_argument("-sV", "--server", action="store_true")
        
        dir.add_argument("-sp", "--show-progress", action="store_true")

        dir.add_argument("-aT", "--application-type", action="store_true")

        dir.add_argument("-wC", "--word-count", action="store_true")
        
        dir.add_argument("-mc", "--match", nargs="*", type=str)
        
        dir.add_argument("-ex", "--exclude",  type=str, nargs="*")
        
        
        vhost = subparser.add_parser("vhost", add_help=False, usage=argparse.SUPPRESS, exit_on_error=False)
        
        vhost.add_argument("-vh", "--vhost-help", action="store_true")
        
        vhost.add_argument("-c", "--concurrency", type=int, default=20)
        
        vhost.add_argument("-sp", "--show-progress", action="store_true")

        vhost.add_argument("-u", "--url", type=str)
        
        vhost.add_argument("-nc", "--no-color", action="store_true")

        vhost.add_argument("-w", "--wordlist", type=str)

        vhost.add_argument("-pX", "--proxy", type=str)

        vhost.add_argument("-o", "--output", type=str)

        vhost.add_argument("-v", "--verbose", action="store_true")

        vhost.add_argument("-t", "--title",action="store_true")

        vhost.add_argument("-tO", "--timeout", type=int)

        vhost.add_argument("-sV", "--server", action="store_true")

        vhost.add_argument("-aT", "--application-type", action="store_true")

        vhost.add_argument("-wC", "--word-count", action="store_true")
        
        vhost.add_argument("-mc", "--match", nargs="*", type=str)
        
        vhost.add_argument("-ex", "--exclude",  type=str, nargs="*")
        
        dns = subparser.add_parser("dns", add_help=False, usage=argparse.SUPPRESS, exit_on_error=False)
        
        dns.add_argument("-dnh", "--dns-help", action="store_true")
        
        dns.add_argument("-d", "--domain", type=str)
        
        dns.add_argument("-w", "--wordlist", type=str)

        dns.add_argument("-o", "--output",  type=str)

        dns.add_argument("-v", "--verbose",  action="store_true")

        dns.add_argument("-sp", "--show-progress", action="store_true")

        dns.add_argument("-c", "--concurrency", type=int, default=20)
        
        doc = subparser.add_parser("doc", add_help=False, usage=argparse.SUPPRESS, exit_on_error=False)
        
        doc.add_argument("-shd", "--show-doc", action="store_true")
        
        
        
        global args 
                
        return parser.parse_args()
        
    
    except argparse.ArgumentError as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Please use the command for more infromation:{reset} {bold}{blue}probuster -h{reset} ")
        
        exit()
        
    except argparse.ArgumentTypeError as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Please use the command for more infromation:{reset} {bold}{blue}probuster -h{reset} ")
        
        exit()
        
        
    except Exception as e:
        
        pass
    
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Probuster exits..{reset}")
        
        exit()
        
        

        

from colorama import Fore,Back,Style


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



def mode_help():
    
    print(f"""
[{bold}{blue}DESCRIPTION{reset}]: {bold}{white}A Python based Web Application Penetration testing tool for Information Gathering{reset}⚡.
          
[{bold}{blue}MODES{reset}]: {bold}{white}
                                  

    - dir   : Directory/file enumeration mode
    - vhost : Virtual host enumeration mode
    - dns   : DNS enumeration mode
    - doc   : Documentation mode for detailed documentation about Probuster
          
[{bold}{blue}Usage{reset}]: {bold}{white}
          
        probuster [commands]
          
    Available Commands:
    
        - dir   : Execute directory/file enumeration mode.
        - vhost : Execute virtual host enumeration mode.
        - dns   : Execute DNS enumeration mode.
        - doc   : Access detailed documentation for Probuster.

    Help Commands:

        - dir   : probuster dir   -dh
        - vhost : probuster vhost -vh
        - dns   : probuster dns   -dnh
        - doc   : probuster doc   -shd

    Notes:

        - For each mode, additional options and flags are available. Use 'probuster [mode] -h' for mode-specific help.

        - Ensure you have the latest version of Probuster for optimal performance and access to the latest features.

        - Ensure with your concurrency value for good results. Probuster performance depends on the User system resources.

        For detailed information about each mode and usage examples, use 'probuster doc --show-doc' or probuster doc -shd.
        \n {reset}""")
    
    
    exit()
    
def dir_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}Directory and Files Enumerations{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            probuster dir [options]
          
        Options for dir mode:
        
               -u,  --url               : Specify the target domain or ip for Directory/File Enumeration mode
               -dh, --dir-help          : Show the help message for Directory Enumeration mode
               -c,  --concurrency       : Set Concurrency level for multiple process for Directory or File enumeration (default: 20)
               -w,  --wordlist          : Wordlist or hostname for Directory or File enumeration
               -pX. --proxy             : Set proxy to pass your request through proxy (ex: 127.0.0.1)
               -o,  --output            : Give a file to save the output for Directory or File enumeration
               -v,  --verbose           : Set Verbose to show output (errors)! 
               -t,  --title             : Get title of the found Directory  or File
               -tO, --timeout           : Set timeout for each request (default 10) 
               -sV. --server            : Get the server name of the found Directory  or File
               -aT, --application-type  : Get the application type of the found Directory  or File
               -wC, --word-count        : Get the word count of the found Directory  or File
               -nc, --no-color          : Disables the colorization output for found results
               -sp. --show-progress     : Enable show prgress mode which will show the progress of the Subprober with progress bar like this ( example: |████████████████████████████████████████| 4000/4000 [100%] in 12.4s (3.23/s) ).
               -mc, --match             : Matches the status code given by user for example: -mc 200 302 
               -ex, --excluded          : Excludes the negative codes and gives user desired results for example: -ex 400 404 500
               
        Notes:
        
            - Probuster Concurrency on Dir/file Enumerations depends on your system resources
            
            - Be careful and gentle with you concurrency value
            
            - Enable desired output flag options for found directories/files
    """)
    
    exit()

    
    
def vhost_mode_help():
    
    print(f"""
[{bold}{blue}MODE{reset}]: {bold}{white}Virtual Host Enumerations{reset}
  
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            probuster vhost [options]
          
        Options for vhost mode:
        
               -u,  --url               : Specify the target ip or host for vitrual host enumeration ( Most probably use IP address as the URL argument)
               -vh, --vhost-help        : Show the help message for Vhost Enumeration mode
               -c,  --concurrency       : Set Concurrency level for multiple process for virtual host enumeration (default: 20)
               -w,  --wordlist          : Wordlist or hostname for brutforce and find virtual host
               -pX. --proxy             : Set proxy to pass your request through proxy (ex: 127.0.0.1)
               -o,  --output            : Give a file to save the output of virtual host enumeration
               -v,  --verbose           : Set Verbose to show output (errors)! 
               -t,  --title             : Get title of the found virtual host 
               -tO, --timeout           : Set timeout for each request (default 10) 
               -sV. --server            : Get the server name of the found virtual host 
               -aT, --application-type  : Get the application type of the found virtual host
               -wC, --word-count        : Get the word count of the found virtual host 
               -nc, --no-color          : Disables the colorization output for found results
               -sp. --show-progress     : Enable show prgress mode which will show the progress of the Subprober with progress bar like this ( example: |████████████████████████████████████████| 4000/4000 [100%] in 12.4s (3.23/s) ).
               -mc, --match             : Matches the status code given by user for example: -mc 200 302 
               -ex, --excluded          : Excludes the negative codes and gives user desired results for example: -ex 400 404 500
               
               
        Notes:
        
             - Virtual host enumeration plays a vital role in expanding your attack vectors
             
             - Virtual host are hiddent host that you may not able to find through some alive subdomains
             
             - Probuster Vhost simplifies the Virtual host enumeration which explained here: https://shorturl.at/berBU
             
             - Probuster will bring new feature for virtual host brutforcing mode in upcoming updates

                          
    """)
    
    exit()
    

def dns_mode_help():
    
    print(f"""
[{bold}{blue}MODE{reset}]: {bold}{white}DNS Enumerations{reset}
  
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            probuster dns [options]   
        
        Options for dns mode:
        
            -d,   --domain            : Domain name for Dns Brutforcing and find subdomains
            -dnh, --dns-help          : Show the help message for DNS Enumeration mode
            -w,   --wordlist          : Wordlist for brutforcing subdomains
            -c,   --concurrency       : Set Concurrency level for multiple process for DNS enumeration (default: 20)
            -v,   --verbose           : Set Verbose to show output (errors)! 
            -o,   --output            : Give a file to save the output of DNS enumeration
            -sp.  --show-progress     : Enable show prgress mode which will show the progress of the Subprober with progress bar like this ( example: |████████████████████████████████████████| 4000/4000 [100%] in 12.4s (3.23/s) ).
            
        Notes:
        
            - Be Gentle with your concurrency value for Dns Enumeration
            
            - If your system is capable to handle high loads with high threads then you can use 1m+ wordlists
            
            - Enable you progress bar to know about the your dns enumeration process
          """)
    
    exit()


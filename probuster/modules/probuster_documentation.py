import streamlit as st
import os 


def get_username():
    
    try:
        
        username = os.getlogin()
        
    except OSError:
       
        username = os.getenv('USER') or os.getenv('LOGNAME') or os.getenv('USERNAME') or 'Unknown User'
        
    except Exception as e:
        
        username = "Unknown User"
        
    
    return username

username = get_username()




st.markdown(f"\n### Welcome to Probuster Documentation {username.upper()} :heart:\n")
st.markdown(f"""---
            
#### Probuster: A Python based Web Application Penetration Tool for Information Gathering and Content Discovery:zap:""")
st.markdown(f"""


Probuster is a cutting-edge reconnaissance toolkit meticulously crafted for ethical hackers, penetration testers, bug bounty hunters and security professionals seeking unparalleled precision in the art of information gathering. This versatile tool seamlessly integrates four distinctive modes, empowering users with unprecedented insights into network landscapes.

**DNS Mode: Unleash the Power of Threaded DNS Enumeration**

In DNS mode, Probuster employs state-of-the-art threaded techniques to perform rapid and comprehensive DNS enumeration. Uncover hidden subdomains, identify potential vulnerabilities, and map the intricate web of domain structures with unparalleled efficiency. Probuster's DNS mode is designed for speed, accuracy, and reliability, ensuring a thorough examination of your target's digital footprint.

**Dir Mode: Elevate Directory and File Enumeration to New Heights**

Probuster's Dir mode elevates directory and file enumeration to new heights. Effortlessly scan web applications for hidden gems, vulnerable endpoints, and critical files. With Probuster's intelligent algorithms and intuitive interface, identify potential security loopholes and streamline your penetration testing workflow with unparalleled ease.

**VHost Mode: Illuminate Virtual Host Structures with Precision**

Illuminate the virtual host landscape using Probuster's VHost mode. Uncover obscured hosts, validate configurations, and gain a granular understanding of the web infrastructure. Probuster's VHost mode delivers accurate virtual host enumeration, enabling security professionals to assess attack surfaces comprehensively and make informed decisions.

**Docs Mode: Explore Comprehensive Documentation with Ease**

Probuster's Docs mode provides a seamlessly integrated documentation hub. Explore comprehensive guides, usage examples, and detailed explanations of each mode. Whether you're a seasoned professional or a beginner, Probuster's documentation ensures that you can harness the full power of the toolkit with confidence.

**Key Features:**

- **Threaded Efficiency:** Probuster harnesses the power of multithreading for rapid and parallelized reconnaissance, ensuring swift and effective scans.
  
- **User-Friendly Interface:** A sleek and intuitive interface facilitates seamless navigation, making Probuster a tool of choice for both novice and seasoned cybersecurity professionals.

- **Customizable Settings:** Tailor Probuster to your specific needs with customizable settings, allowing fine-tuning for different environments and scenarios.

- **Comprehensive Reporting:** Generate detailed reports that encapsulate findings, aiding in concise communication of discovered vulnerabilities and potential risks.

Probuster is not just a tool, it's a manifestation of excellence in reconnaissance, designed to empower ethical hackers with the precision needed to navigate the complexities of modern cybersecurity landscapes. Elevate your penetration testing capabilities with Probuster and redefine your approach to ethical hacking. 

### Version 1.0.2 Update:

- Unlike updating from version 1.0.1 to 1.0.2 , Probuster new version is updated and recoded from the scratch

- Unlike Previous Versions traditional threading , Probuster new version converted to asynchronous performance and high in concurrent
  for all modes
  
- Command line structure and command line arguments are changed for all modes in probuster new Version

- Introduced new mode `Update` so users can update the probuster to new versions
---

### Contributor:

- [Xer](https://www.linkedin.com/in/aslamx3r) contributed in probuster new version for enhancing the output methods and cli's arguments

---
""")

st.markdown(f"""
            
### Main Usage:
```yaml
probuster -h                                                                    

8888888b.                   888888b.                     888                     
888   Y88b                  888  "88b                    888                     
888    888                  888  .88P                    888                     
888   d88P 888d888  .d88b.  8888888K.  888  888 .d8888b  888888  .d88b.  888d888 
8888888P"  888P"   d88""88b 888  "Y88b 888  888 88K      888    d8P  Y8b 888P"   
888        888     888  888 888    888 888  888 "Y8888b. 888    88888888 888     
888        888     Y88..88P 888   d88P Y88b 888      X88 Y88b.  Y8b.     888     
888        888      "Y88P"  8888888P"   "Y88888  88888P'  "Y888  "Y8888  888     
                                                                                 
                                                                                 
                                                                                 

    
                     Author : D.SanjaiKumar @CyberRevoltSecurities


[DESCRIPTION]: A Python based Web Application Penetration testing tool for Information Gathering and Content Discovery⚡.
          
[MODES]: 
                                  

    - dir         : Directory/file enumeration mode
    - vhost       : Virtual host enumeration mode
    - dns         : DNS enumeration mode
    - doc         : Documentation mode for detailed documentation about Probuster
    - update      : Update the Probuster to latest version
    - Version     : Shows the Probuster current Version
    
[FLAGS]: 

    -h,  --help   : Shows this help message and exits.
              
[Usage]: 
          
        probuster [commands]
          
    Available Commands:
    
        - dir     : Execute directory/file enumeration mode.
        - vhost   : Execute virtual host enumeration mode.
        - dns     : Execute DNS enumeration mode.
        - doc     : Access detailed documentation for Probuster.
        - update  : Updates the Probuster to latest version

    Help Commands:

        - dir     : probuster dir   -h
        - vhost   : probuster vhost -h
        - dns     : probuster dns   -h
        - doc     : probuster doc   -h
        - update  : probuster update -h

    Notes:

        - For each mode, additional options and flags are available. Use 'probuster [mode] -h' for mode-specific help.

        - Ensure you have the latest version of Probuster for optimal performance and access to the latest features.

        - Ensure with your concurrency value for good results. Probuster performance depends on the User system resources.

        For detailed information about each mode and usage examples, use 'probuster doc --show-doc' or probuster doc -shd.


```
Probuster's main usage help serves as a gateway to its robust features. Use the command structure `probuster [commands]` to access specialized modes like `dir` for directory enumeration, `vhost` for virtual host analysis, and `dns` for threaded DNS enumeration. Additionally, explore detailed documentation effortlessly with the `doc` mode. Tailor your commands, leverage advanced features, and elevate your web application penetration testing with Probuster.
Lets see some more information about all probuster modes and their usages for more detailed explaination see in below.

""")

st.markdown(f"""
---
### Probuster dir Mode Usage:

```yaml
probuster dir -h

 ___            ___            _             
| _ \ _ _  ___ | _ ) _  _  ___| |_  ___  _ _ 
|  _/| '_|/ _ \| _ \| || |(_-<|  _|/ -_)| '_|
|_|  |_|  \___/|___/ \_,_|/__/ \__|\___||_|  


[Version]: Probuster current version v1.0.2 (latest)

[MODE]: Directory and Files Enumerations
            
[Usage]: 
          
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
               -ar. --allow-redirect    : Enabling it will make probuster to follow redirects 
               -mc, --match             : Matches the status code given by user for example: -mc 200 302 
               -ex, --excluded          : Excludes the negative codes and gives user desired results for example: -ex 400 404 500               
        Notes:
        
            - Probuster Concurrency on Dir/file Enumerations depends on your system resources
            
            - Be careful and gentle with you concurrency value
            
            - Enable desired output flag options for found directories/files (ex: --title, --server, --application-type, --word-count, --match)


```

### Dir Mode Examples:


```yaml
probuster dir -u http://test.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o dirfile.txt -c 500  -ex 404 -sp  --title --server --application-type -wC


 ___            ___            _             
| _ \ _ _  ___ | _ ) _  _  ___| |_  ___  _ _ 
|  _/| '_|/ _ \| _ \| || |(_-<|  _|/ -_)| '_|
|_|  |_|  \___/|___/ \_,_|/__/ \__|\___||_|  


[Version]: Probuster current version v1.0.2 (latest)

              
========================================================================================
[!]User        : {username}

[!]Mode        :  Directory or File Enumeration                                              
                                                                                       
[!]URL         : http://test.com          

[!]Wordlist    : /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt                                               
                                                                                       
[!]Concurrency : 500                                                    
                                                                                       
[!]Time-Out    : None                                                        
                                                                                       
========================================================================================

http://test.com/images [403] [Apache] [text/html] [403:Forbidden] [165]
http://test.com/js [403] [Apache] [text/html] [403:Forbidden] [165]
http://test.com/documentation [403] [Apache] [text/html] [403:Forbidden] [165]
http://test.com/dashboard [200] [Apache] [text/html] [Admin Dashboard] [2080]
http://test.com/javascript [403][Apache] [text/html] [403:Forbidden] [165]
http://test.com/javascript [403] [Apache] [text/html] [403:Forbidden] [165]

|██████████████████████████████████  | 3598/4000 [80%] in 12.4s (3.23/s) 
```
---
""")

st.markdown(f"""
            
### Probuster dns Mode Usage:

```yaml
probuster dns -h


   ___                 ___              _               
  / _ \ _ __   ___    / __\ _   _  ___ | |_   ___  _ __ 
 / /_)/| '__| / _ \  /__\//| | | |/ __|| __| / _ \| '__|
/ ___/ | |   | (_) |/ \/  \| |_| |\__ \| |_ |  __/| |   
\/     |_|    \___/ \_____/ \__,_||___/ \__| \___||_|   
                                                        

                                                                     
[Version]: Probuster current version v1.0.2 (latest)

[MODE]   : DNS Enumerations

[Usage]  : probuster dns [options]

[MODE]: DNS Enumerations
  
[Usage]: 
          
            probuster dns [options]   
        
        Options for dns mode:
        
            -d,   --domain            : Domain name for Dns Brutforcing and find subdomains
            -dnh, --dns-help          : Show the help message for DNS Enumeration mode
            -w,   --wordlist          : Wordlist for brutforcing subdomains
            -c,   --concurrency       : Set Concurrency level for multiple process for DNS enumeration (default: 20)
            -v,   --verbose           : Set Verbose to show output (errors)! 
            -o,   --output            : Give a file to save the output of DNS enumeration
            -sip, --show-ip           : Enable --show-ip will show the ip address of the found subdomain
            -nc, --no-color           : Enable --no-color will print the output without any colors
            
        Notes:
        
            - Be Gentle with your concurrency value for Dns Enumeration
            
            - If your system is capable to handle high loads with high threads then you can use 2m+ wordlists
            
            - Enable you progress bar to know about the your dns enumeration process
```
---""")

st.markdown(f"""
### Dns Mode Examples:

```yaml

probuster dns -d microsoft.com -c 20 -o test.txt -w ~/wordlists/subdomains/subdomains1.txt -sp 


   ___                 ___              _               
  / _ \ _ __   ___    / __\ _   _  ___ | |_   ___  _ __ 
 / /_)/| '__| / _ \  /__\//| | | |/ __|| __| / _ \| '__|
/ ___/ | |   | (_) |/ \/  \| |_| |\__ \| |_ |  __/| |   
\/     |_|    \___/ \_____/ \__,_||___/ \__| \___||_|   
                                                        


[Version]: Probuster current version v1.0.2 (latest)
========================================================================================
[!]User        : {username}

[!]Mode        : DNS Enumeration                                              
                                                                                       
[!]Doamin      : microsoft.com          

[!]Wordlist    : /home/user/wordlists/subdomains/subdomains.txt                                               
                                                                                       
[!]Concurrency : 20                                                                                                         
                                                                                       
========================================================================================             
                  
                  
[FOUND]: www.microsoft.com
[FOUND]: s.microsoft.com
[FOUND]: i.microsoft.com
[FOUND]: connect.microsoft.com
[FOUND]: connect.microsoft.com
[FOUND]: assets.microsoft.com
[FOUND]: maps.microsoft.com
[FOUND]: cdn.microsoft.com
[FOUND]: api.microsoft.com
|███                 | 3998/400000 [20%] in 12.4s (3.23/s)
```
---""")

st.markdown(f"""
### Probuster Vhost Mode Usage:

```yaml
probuster vhost -h

 , __             , __                          
/|/  \           /|/  \                         
 |___/ ,_    __   | __/        ,  _|_  _   ,_   
 |    /  |  /  \_ |   \|   |  / \_ |  |/  /  |  
 |       |_/\__/  |(__/ \_/|_/ \/  |_/|__/   |_/



[Version]: Probuster current version v1.0.2 (latest)

[MODE]: Virtual Host Enumerations
  
[Usage]: 
          
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
               -aT, --application-type  : Get the server name of the found virtual host
               -wC, --word-count        : Get the word count of the found virtual host 
               -nc, --no-color          : Disables the colorization output for found results
               -ar, --allow-redirect    : Enabling it will make probuster to follow redirects 
               -mc, --match             : Matches the status code given by user for example: -mc 200 302 
               -ex, --excluded          : Excludes the negative codes and gives user desired results for example: -ex 400 404 500
               
               
        Notes:
        
             - Virtual host enumeration plays a vital role in expanding your attack vectors
             
             - Virtual host are hiddent host that you may not able to find through some alive subdomains
             
             - Probuster Vhost simplifies the Virtual host enumeration which explained here: https://shorturl.at/berBU
             
             - Probuster will bring new feature for virtual host brutforcing mode in upcoming updates


```
---""")

st.markdown(f"""
### Vhost Mode Examples:

```yaml
probuster vhost -u https://20.236.44.162 -tO 5 -c 100 -sp -w ~/Desktop/Bugbounty/public/microsoft/all_subdomains.txt --server --title -aT -wC --output output.txt

 , __             , __                          
/|/  \           /|/  \                         
 |___/ ,_    __   | __/        ,  _|_  _   ,_   
 |    /  |  /  \_ |   \|   |  / \_ |  |/  /  |  
 |       |_/\__/  |(__/ \_/|_/ \/  |_/|__/   |_/



[Version]: Probuster current version v1.0.2 (latest)

========================================================================================
[!]User        : {username}

[!]Mode        : Virtual Host Enumeration                                              
                                                                                       
[!]URL         : https://20.236.44.162          

[!]Wordlist    : /home/user/Desktop/Bugbounty/public/microsoft/all_subdomains.txt                                               
                                                                                       
[!]Concurrency : 100                                                  
                                                                                       
[!]Time-Out    : 5                                                        
                                                                                       
========================================================================================

academic.microsoft.com [400] [AkamaiGHost] [text/html] [Invalid URL] [13]
Academic.microsoft.com [400] [AkamaiGHost] [text/html] [Invalid URL] [13]
Academy.microsoft.com [400] [AkamaiGHost] [text/html] [Invalid URL] [13]
academy.techcommunity.microsoft.com [400] [AkamaiGHost] [text/html] [Invalid URL] [13]
academy.microsoft.com [400] [AkamaiGHost] [text/html] [Invalid URL] [13]
academy.microsoft.com [400] [AkamaiGHost] [text/html] [Invalid URL] [13]
|█████▌                                 | 12611/91392 [14%] in 8:27.5 (24.85/s)

```
---""")

st.markdown(f"""

## Probuster GitHub Repository

Head over to the [Probuster GitHub repository](https://github.com/sanjai-AK47/Probuster). Dive into the code, contribute your expertise, and share your experiences and feedback. This tool is a collaborative effort, 
## About the Author

I'm D. Sanjai Kumar, the creator of Probuster. I'm passionate about advancing cybersecurity, and Probuster is a testament to that passion. Connect with me on [LinkedIn](https://www.linkedin.com/in/d-sanjai-kumar-109a7227b).

## Show Your Support

If Probuster has rocked your ethical hacking world, let's spread the love! Give the repository a star :star: on [GitHub](https://github.com/sanjai-AK47/Probuster). Share it with your network, and let's build a community around this tool.

Got feedback, suggestions, or want to contribute? Reach out to me directly. Let's keep pushing the boundaries of cybersecurity and innovation together.

Thank you for choosing Probuster. Now, go out there and hack responsibly!

---
**Disclaimer:** 
Probuster is designed for ethical hacking and penetration testing. Any use for malicious activities is strictly prohibited.
""")
st.markdown(f"---")
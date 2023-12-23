from .modules.handler import handler

def main():
    
    try:
    
        handler()
        
    except Exception as e:
        
        exit()
    
if __name__ == "__main__":
    
    main()
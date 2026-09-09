from config import HAR_ROOT_PATH, LABELLED_FILE, FINAL_FILE
from collector import collect_hars
from hunter import hunt_hars
import sys

USAGE = """Usage:
    python3 main.py <collect|hunt>
"""

def main():
    
    args = sys.argv[1:]
 
    if len(args) == 1:
        
        if args[0] == "collect":
            
            collect_hars(HAR_ROOT_PATH)
            
        elif args[0] == "hunt":
            
            final = hunt_hars(HAR_ROOT_PATH, LABELLED_FILE)
            final.to_csv(FINAL_FILE, index=False)
            
        else:
            
            print(USAGE)
            sys.exit(1)
        
    else:
        
        print(USAGE)
        sys.exit(1)
 
 
if __name__ == "__main__":
    main()
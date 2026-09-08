from config import HAR_ROOT_PATH, COLLECTOR_PATH, CLASSIFICATION_PATH, LABELED_PATH, FINAL_PATH
from extraction import extract_all
from classification import label_all
import sys

USAGE = """Usage:
    python3 main.py <extract|label>
"""

def main():
    
    args = sys.argv[1:]
 
    if len(args) == 1:
        
        if args[0] == "extract":
            
            collector, classification = extract_all(HAR_ROOT_PATH)
            
            collector.to_csv(COLLECTOR_PATH, index=False)
            classification.to_csv(CLASSIFICATION_PATH, index=False)
            
        elif args[0] == "label":
            
            final = label_all(COLLECTOR_PATH, LABELED_PATH)
            final.to_csv(FINAL_PATH, index=False)
            
        else:
            
            print(USAGE)
            sys.exit(1)
        
    else:
        
        print(USAGE)
        sys.exit(1)
 
 
if __name__ == "__main__":
    main()
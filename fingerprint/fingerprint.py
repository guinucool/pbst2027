import json
import os

# Input output ========================================
# Markdown for fingerprinting apis, source: https://github.com/uiowa-irl/FP-Inspector/blob/master/Data/potential_fingerprinting_APIs.md
FP_APIS_MD: str = str(os.path.dirname(__file__)) + "/input/potential_fingerprinting_APIs.md"
# Cleaned apis file from markdown
FP_APIS_CLEAN: str = str(os.path.dirname(__file__)) + "/input/fp-inspector_apis.txt"
# Captures folder
CAPTURES_FOLDER: str = str(os.path.dirname(__file__)) + "/../data/samples/"
# Output file
FPRINTERS_FILE = str(os.path.dirname(__file__)) + "/../data/results/tests/fingerprinters.json"

def extra_filter(api: str,file_path: str):
    """Filter called always to add especial cases, if returns false it is a false positive"""
    if api == "magnetometer":
        # If the api is magnetometer filter out false positives that are in the permisions policy
        # Goes through whole file searching for a hit that is not preceeded by permissions policy
        with open(file_path, 'r', encoding='utf-8') as file:
            previous_line = None
            for current_line in file:
                # Check if the target string is in the current line
                if api in current_line.lower():
                    if previous_line is not None:
                        if not '"name": "permissions-policy",' in previous_line:
                            return True
                        
                # Update previous_line for the next iteration
                previous_line = current_line
        
        return False
                
    return True

def search_api_in_captures(folder: str,value: str)->set[str]:
    """
    Search HAR files for a value and return matching organizations.

    Args:
        folder: Directory containing HAR captures.
        value: Value to search for.

    Returns:
        Set of matching organization names.
    """
    
    orgs: set[str] = set()
    for folder, dirs, files in os.walk(folder): # type: ignore
        for file in files:
            # Check har files (network)
            if file.endswith('.har'):
                # Get full path
                fullpath = os.path.join(folder, file)
                with open(fullpath, 'r') as f:
            
                    for line in f:                  
                        if value in line.lower():
                            
                            # Process folder name to obtain device and agent
                            split = fullpath.split('/')
                            
                            org = split[9].lower().capitalize()
                            if 'mobile' in split[8]:
                                org = org + "-" + 'Mobile'
                            else:
                                org = org + "-" + 'Web'
                            
                            # Check for filter and already added
                            if org not in orgs and extra_filter(value, fullpath):
                                orgs.add(org)
                                print(org)
                                print(fullpath)
                            break
    return orgs
                
def get_fp_apis(folder: str, api_list: list[str])->dict[str, set[str]]:
    """
    Search capture files for multiple APIs and map each API to matching organizations.

    Args:
        folder: Directory containing HAR captures.
        api_list: APIs to search for.

    Returns:
        Mapping of API names to sets of matching organizations.
    """
    print(f"Searching in {folder}")
    
    api_org: dict[str,set[str]] = dict()
    for api in api_list:
        print(f"-----{api}-----")
        api_org[api] = search_api_in_captures(folder, api.lower())
        
    return api_org
        
def main():
    # Get the list of apis
    api_list: list[str] = list()
    with open(FP_APIS_CLEAN, "r") as f:
        for line in f.readlines():
            api_list.append(line.split()[0])
            
    print(api_list)
    
    fingerpringters = get_fp_apis(CAPTURES_FOLDER, api_list)
    
    with open(FPRINTERS_FILE, "w+") as f:
        json.dump(fingerpringters, f, default=list, indent=4)

    
if __name__ == "__main__":
    main()
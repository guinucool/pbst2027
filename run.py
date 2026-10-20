import os
import subprocess
import sys
 
ROOT = os.path.dirname(__file__)
WIDTH = 60
 
def title(text):
    print("\n" + "=" * WIDTH)
    print(text.center(WIDTH))
    print("=" * WIDTH)
 
 
def subtitle(text):
    print(f"\n--- {text} ---")
 
def run(script, *args):
    
    cmd = [sys.executable, script, *args]
    print(f"\n>>> {' '.join(cmd)}")
    
    try:
        
        subprocess.run(cmd, cwd=ROOT, check=True)
        
    except subprocess.CalledProcessError as e:
        
        print(f"\nError: '{' '.join(cmd)}' exited with code {e.returncode}. Aborting.")
        sys.exit(e.returncode)
 
 
def main():
    
    # Experiment 1: Third-party Service Analysis
    title("Experiment 1: Third-party Service Analysis")
 
    subtitle("Extracting third-party domains")
    run("tpintegration/main.py", "extract")
 
    input(
        "\nThe extraction stage generated 'tp_classification.csv'.\n"
        "Label the domains and save the result as 'tp_labelled.csv', "
        "then press Enter to continue..."
    )
    
    subtitle("Labeling domains")
    run("tpintegration/main.py", "label")
    
    subtitle("Generating the integration graph")
    run("tpintegration/graph.py")
 
    # Experiment 2: Privacy Analysis
    title("Experiment 2: Privacy Analysis")
 
    subtitle("Collecting predictable identifiers")
    run("privacyanalysis/main.py", "collect")
    
    subtitle("Inspecting for dissemination")
    run("privacyanalysis/main.py", "hunt")
 
    # Experiment 3: Fingerprint Analysis
    title("Experiment 3: Fingerprint Analysis")
 
    subtitle("Extracting fingerprinting APIs")
    run("fingerprint/fingerprint.py")
 
    # Validation
    title("Validation")
    answer = input("\nAll experiments finished. Run the check script? [y/N] ").strip().lower()
    
    if answer in ("y", "yes"):
        run("data/results/check.py")
    else:
        print("Skipping the check script.")
 
 
if __name__ == "__main__":
    main()
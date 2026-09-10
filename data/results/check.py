import hashlib

TESTS = [
    ("Third-Party Integration: Exctraction (Collector)", "tests/tp_collector.csv", "expected/tp_collector.csv", "expected/tp_collector_alt.csv"),
    ("Third-Party Integration: Exctraction (Classification)", "tests/tp_classification.csv", "expected/tp_classification.csv", "expected/tp_classification_alt.csv"),
    ("Third-Party Integration: Labelling", "tests/tp_final.csv", "expected/tp_final.csv", "expected/tp_final_alt.csv"),
    ("Third-Party Integration: Graph", "tests/tp_graph.png", "expected/tp_graph.png"),
    ("Privacy Analysis: Collection (C1-I1)", "../samples/WEB/GROK/GROK-A2-P1-T1-C1-S2-20260901/I1/collected.val", "expected/collected-C1-I1.val"),
    ("Privacy Analysis: Collection (C1-I2)", "../samples/WEB/GROK/GROK-A2-P1-T1-C1-S2-20260901/I2/collected.val", "expected/collected-C1-I2.val"),
    ("Privacy Analysis: Collection (C2-I1)", "../samples/WEB/GROK/GROK-A2-P1-T1-C2-S2-20260901/I1/collected.val", "expected/collected-C2-I1.val"),
    ("Privacy Analysis: Collection (C2-I2)", "../samples/WEB/GROK/GROK-A2-P1-T1-C2-S2-20260901/I2/collected.val", "expected/collected-C2-I2.val"),
    ("Privacy Analysis: Collection (C3-I1)", "../samples/WEB/GROK/GROK-A2-P1-T1-C3-S2-20260901/I1/collected.val", "expected/collected-C3-I1.val"),
    ("Privacy Analysis: Collection (C3-I2)", "../samples/WEB/GROK/GROK-A2-P1-T1-C3-S2-20260901/I2/collected.val", "expected/collected-C3-I2.val"),
    ("Privacy Analysis: Hunter", "tests/pa_final.csv", "expected/pa_final.csv"),
    ("Fingerprinting", "tests/fingerprinters.json", "expected/fingerprinters.json")
]

CHUNK_SIZE = 8192

def calculate_md5(file_path):
    
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as f:
        
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            
            md5_hash.update(chunk)

    return md5_hash.hexdigest()


def check_results(tests):
    
    for test in tests:
        
        title, result, *expected_files = test
        
        try:
            
            result_hash = calculate_md5(result)
        
        except FileNotFoundError as _:
            
            print(f"{title} - Experiment not performed.") 
            continue  
        
        matched = False

        for expected in expected_files:
            
            expected_hash = calculate_md5(expected)
                
            if result_hash == expected_hash:
                
                matched = True
                break

        if matched is True:
            
            print(f"{title} - Correct.")
            
        else:
            
            print(f"{title} - Failed.")

if __name__ == "__main__":
    check_results(TESTS)
import sys

def get_filename():
    try:
        return sys.argv[1]
    except IndexError:
        print("Usage: python Day 7 Mini-Project.py <logfile>")
        sys.exit()

def read_log_file(filename):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(" Log File Not Found")
        sys.exit()

def Analyse_results(lines):
    failed = {}
    success = {}

    for line in lines:
        ip, status = line.split()

        if status == "FAILED":
            failed[ip] = failed.get(ip, 0) + 1
        elif status == "SUCCESS":
            success[ip] = success.get(ip, 0) + 1
        
    return failed, success
        

def report_results(failed,success, threshold=2):
    print("=== Login Summary ===")
    print(f"Total Failed Logins {sum(failed.values())}")
    print(f"Total Successful Login {sum(success.values())}")

    print("=== Suspicious Logins ===")
    for ip, count in failed.items():
        if count > threshold:
            print(f"{ip} ({count} failed attempts)" )
    

def main():
    filename = get_filename()
    lines = read_log_file(filename)
    failed, success = Analyse_results(lines)
    report_results(failed=failed, success=success)
    

if __name__ == "__main__":
    main()

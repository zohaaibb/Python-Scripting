failed_ip = {}

with open("access.log", "r") as file:
    for line in file:
        if "Failed" in line:
            ip = line.split()[0]
            failed_ip[ip] = failed_ip.get(ip, 0) + 1

for ip, count in failed_ip.items():
    print(ip, count)


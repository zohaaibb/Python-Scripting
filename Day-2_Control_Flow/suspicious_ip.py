# Dictionary Created of Suspicious IPs with failed login attempts
dict_ip = {
    "192.168.100.1": 3,
    "192.168.100.2": 5,
    "192.168.100.3": 7,
    "192.168.100.4": 10
}

for ip, count in dict_ip.items():
    if count > 5:
        print(f"{ip} is suspicious")
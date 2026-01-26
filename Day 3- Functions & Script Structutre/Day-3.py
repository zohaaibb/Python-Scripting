dict_ip = {
    "192.168.100.1": 3,
    "192.168.100.2": 5,
    "192.168.100.3": 7,
    "192.168.100.4": 10
}

def is_suspicious(count):
    return count > 5

def checking():
    for ip, count in dict_ip.items():
        if is_suspicious(count):
            print(f"{ip} is suspicious")

if __name__ == "__main__":
    checking()

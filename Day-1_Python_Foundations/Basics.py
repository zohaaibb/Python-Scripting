print("Hello Cyber World")


username = input("What is your name: ")
password = input("What is your password: ")
print(f"Attempting login for {username}")


ip = input("Enter IP address: ")
fail = int(input("Enter failed attempts: "))


ip_dict = {}
ip_dict[ip] = fail


print(f"IP {ip} has {fail} failed logins")
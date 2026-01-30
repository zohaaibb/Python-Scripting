import sys
import socket


try:
    ip = sys.argv[1]
    port = sys.argv[2]
except IndexError:
    print("Usage: client.py <ip> <port>")
    sys.exit()
except ValueError:
    print("The Port Must be a number")
    sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)


try:
    s.connect((ip, port))
    s.send(b" HELLO SERVER ")

    raw_data = s.recv(1024)
    decoded_data = raw_data.decode()
    print(f" The Data Recieved is {decoded_data}")

except socket.timeout:
    print(" The Server did not respond on time")

except ConnectionRefusedError:
    print(" The Server refused the connection")

except Exception as e:
    print(f"Error as {e}")

finally:
    s.close()

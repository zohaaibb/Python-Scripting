# Day 8 – Socket Programming: TCP Client

## 📌 Objective
Learn how to communicate with a server using Python sockets.  

- Connect to a server
- Send a message
- Receive a response
- Handle timeouts and errors

---

## 🧠 What is a Socket?

A **socket** is an endpoint for sending and receiving data between two machines over a network.  

- It’s like a **virtual cable** connecting two programs.
- One side **listens** (server), the other side **connects** (client).
- Sockets are the foundation of most network applications:
  - Web servers
  - Chat apps
  - Network scanners
  - Remote administration tools

---

### 🔹 TCP vs UDP
| Type | Description |
|------|-------------|
| TCP (`SOCK_STREAM`) | Reliable, ordered connection. Guarantees delivery. Used in web, email, file transfer |
| UDP (`SOCK_DGRAM`) | Unreliable, connectionless. Faster. Used in streaming, gaming, DNS queries |

---

## ▶️ How It Works in This Script

1. Create a socket:
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Connect to server:
```python
s.connect((IP, PORT))
```

Send data as bytes:
```python
s.send(b"HELLO SERVER")
```

Receive data (up to 1024 bytes):
```python
response = s.recv(1024)
```

Decode bytes to string and print.

Handle exceptions:
```python
ConnectionRefusedError

socket.timeout

FileNotFoundError (if reading from a file)
```
Close socket:
```python
s.close()
```
## ▶️ How to Run
python client.py <IP> <PORT>


Example:

python client.py 127.0.0.1 9999

## 💡 Notes

The server must be running and listening on the IP/PORT

Timeout is set to 3 seconds

Only works with TCP servers

Sending/receiving is always done in bytes, not strings

## ❓ Reflection Questions

What does AF_INET mean?

What does SOCK_STREAM mean?

Why do we send bytes and not strings?

What happens if the recv() buffer is too small?


---

This gives **complete context** about sockets for anyone checking your repo, and it’s **professional enough for LinkedIn or GitHub showcase**.  

If you want, I can now **create a Day 8 server script README + threaded server** so your client has a real server to talk to and you can test it end-to-end.  

Do you want me to do that next?

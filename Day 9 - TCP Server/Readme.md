# Day 9 – Socket Programming: TCP Server

## 📌 Objective
Learn how to accept client connections using Python sockets.  

- Listen for connections
- Accept a client
- Receive and send messages
- Understand the difference between server and client sockets

---

## 🧠 Key Concepts
- `bind()` → attach server to IP + port  
- `listen()` → start waiting for connections  
- `accept()` → accept a connection, returns `(conn, addr)`  
- `conn` → dedicated client socket  
- `addr` → client IP + port  
- `recv()` / `send()` → communicate with client  

---

## ▶️ How It Works

1. Create socket:  
```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
2.Bind:
```python
server.bind(("127.0.0.1", 9999))
```

3.Listen:
```python
server.listen(1)
```

4.Accept client:
```python
conn, addr = server.accept()
```
5.Receive data:
```python
data = conn.recv(1024)
```

6.Send response:
```python
conn.send(b"HELLO CLIENT")
```

7.Close connection & server:
```python
conn.close()
server.close()
```

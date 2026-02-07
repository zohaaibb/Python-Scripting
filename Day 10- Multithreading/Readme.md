# Day 10 – Multi-Client TCP Server (Threading)

## 📌 Objective
Build a TCP server that can handle **multiple clients simultaneously** using Python threading.

---

## 🧠 Key Concepts Learned

### 🔹 Threading
- Each client connection runs in its **own thread**
- Prevents the server from blocking on a single client

### 🔹 Server Flow

---

## 🔧 How the Server Works

1. Server listens on `127.0.0.1:9999`
2. When a client connects:
   - Server accepts the connection
   - A new thread is created
   - Client is handled independently
3. Server continues listening for new clients

---

## ▶️ How to Run

### Start the Server
```bash
python server.py
```

### Run Multiple Clients (in separate terminals)
```python
python client.py 127.0.0.1 9999
```

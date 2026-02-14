# 🐍 Python Threaded Port Scanner

A simple multi-threaded TCP port scanner built using Python's `socket` and `threading` modules.

This project was created as part of learning:

- Socket programming
- TCP connections
- Multithreading
- Basic network scanning concepts
- Git & GitHub workflow

---

## 🚀 Features

- Scans ports 1–100
- Uses `socket.connect_ex()` to check port status
- Uses multithreading for faster scanning
- Each port runs in its own thread
- Waits for all threads to finish using `join()`

---

## 🧠 How It Works

1. The user provides a target IP address as a command-line argument.
2. A function `scan_port(port)`:
   - Creates a TCP socket
   - Attempts connection to the target and port
   - Prints open ports
   - Closes the socket
3. The main program:
   - Creates a thread for each port (1–100)
   - Starts all threads
   - Waits for them to complete using `join()`

---

## 🖥️ Usage

```bash
python port_scanner.py <target_ip>

# Day 4 – File Handling & Dictionaries

## 📌 What You Learn on Day 4

Day 4 focuses on **reading files**, **updating dictionaries safely**, and writing cleaner logic using `dict.get()` instead of messy `if/else` blocks.

---

## 🔹 Reading Files in Python

Files are commonly used to store logs, outputs, or input data.

### Basic File Reading

```python
with open("access.log", "r") as file:
    for line in file:
        print(line)
```

Why `with` is important:

* Automatically closes the file
* Prevents memory leaks
* Cleaner and safer

---

## 🔹 Dictionaries Recap

Dictionaries store data as **key-value pairs**.

```python
failed_ip = {}
```

* Key → IP address
* Value → Number of failed attempts

---

## 🔹 Problem: Counting Failed Attempts

When parsing logs, an IP may appear multiple times.
We must:

* Add the IP if it does not exist
* Increment the count if it already exists

---

## 🔹 Traditional if/else Approach

```python
if ip in failed_ip:
    failed_ip[ip] = failed_ip[ip] + 1
else:
    failed_ip[ip] = 1
```

Works, but:

* Verbose
* Repetitive
* Not clean for large scripts

---

## 🔹 Cleaner Approach: dict.get()

```python
failed_ip[ip] = failed_ip.get(ip, 0) + 1
```

### How this works

* `failed_ip.get(ip, 0)`:

  * Returns the value if `ip` exists
  * Returns `0` if `ip` does not exist
* Then we add `1`

This replaces the entire `if/else` block.

---


## 🔹 Threshold Concept

A threshold is a **limit value** used to decide when something becomes suspicious.

```python
threshold = 3

if count > threshold:
    print(f"{ip} is suspicious")
```

Changing the threshold changes detection behavior **without changing logic**.

---

## 🧠 Key Takeaways

* Always use `with open()` for files
* `dict.get()` simplifies logic
* Dictionaries are ideal for counting
* Thresholds make scripts flexible

---



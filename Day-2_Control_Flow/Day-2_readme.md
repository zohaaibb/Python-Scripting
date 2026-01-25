# 📘 Day 2 – Control Flow & Logic

Day 2 is about **making decisions in code**. Instead of Python just running line by line, we teach it:

* when to act
* when to skip
* how to repeat tasks

This is the foundation of **all scripting and automation**.

---

## 🔹 What is Control Flow?

Control flow decides **which code runs and when**.

In Python, this is done using:

* `if / else`
* loops (`for`, `while`)

---

## 🔹 Conditional Statements (`if`, `else`)

Python can make decisions based on conditions.

```python
failed_attempts = 7

if failed_attempts > 5:
    print("Suspicious activity detected")
else:
    print("Normal activity")
```

* `if` checks a condition
* Code runs **only if the condition is true**
* Indentation is mandatory

---

## 🔹 Comparison Operators

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | equal to         |
| `!=`     | not equal        |
| `>`      | greater than     |
| `<`      | less than        |
| `>=`     | greater or equal |
| `<=`     | less or equal    |

---

## 🔹 Loops (Repeating Code)

### `for` Loop

Used to iterate over collections like lists and dictionaries.

```python
ports = [22, 80, 443]

for port in ports:
    print(port)
```

---

## 🔹 Looping Through a Dictionary

```python
dict_ip = {
    "192.168.100.1": 3,
    "192.168.100.2": 5,
    "192.168.100.3": 7
}

for ip, count in dict_ip.items():
    print(ip, count)
```

* `.items()` gives **key + value** together
* `ip` → dictionary key
* `count` → dictionary value

---

## 🧪 Day 2 Example Code (`suspicious_ips.py`)

```python
dict_ip = {
    "192.168.100.1": 3,
    "192.168.100.2": 5,
    "192.168.100.3": 7,
    "192.168.100.4": 10
}

for ip, count in dict_ip.items():
    if count > 5:
        print(f"{ip} is suspicious")
```



# Day 5 – Command Line Arguments (sys.argv)

## 📌 What You Learn on Day 5

Day 5 introduces **command-line arguments**, allowing Python scripts to accept input **when the script is run**, not while it is executing.

This is essential for:

* Automation
* Reusable scripts
* Running tools on different files without editing code

---

## 🔹 What is `sys.argv`

`sys.argv` is a **list** that stores command-line arguments.

To use it, we must import the `sys` module:

```python
import sys
```

---

## 🔹 Understanding `sys.argv`

When you run:

```bash
python test.py file.txt 5
```

Python creates this list:

```python
sys.argv = ["test.py", "file.txt", "5"]
```

### Important Rules

* `sys.argv[0]` → script name
* `sys.argv[1]` → first argument
* `sys.argv[2]` → second argument

All values are **strings**.

---

## 🔹 Basic Example

```python
import sys

print(sys.argv)
```

Run:

```bash
python test.py hello world
```

Output:

```text
['test.py', 'hello', 'world']
```

---

## 🔹 Using Arguments in a Script

```python
import sys

log_file = sys.argv[1]
threshold = int(sys.argv[2])

print(f"Log file: {log_file}")
print(f"Threshold: {threshold}")
```

⚠️ If arguments are missing, Python raises an error.

---

## 🔹 Preventing Errors (Length Check)

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <logfile> <threshold>")
    sys.exit()
```

This avoids:

```text
IndexError: list index out of range
```

---




## 🧠 Key Takeaways

* `sys.argv` is a list
* Indexing starts at 0
* All arguments are strings
* Always validate argument length

---

# Day 6 – Error Handling & Defensive Scripting

## 📌 What You Learn on Day 6

Day 6 introduces **error handling** using `try/except` and how to make your scripts **robust**.

Scripts in the real world crash if:

* User input is invalid
* Files don’t exist
* Command-line arguments are missing
* Log files are malformed

We learn how to **prevent crashes** gracefully.

---

## 🔹 Basic try/except

```python
try:
    x = int("hello")
except ValueError:
    print("Input was not a number")
```

* `try` → risky code
* `except` → handles specific errors

---

## 🔹 Handling missing command-line arguments

```python
import sys

try:
    filename = sys.argv[1]
except IndexError:
    print("Please provide a filename")
    sys.exit()
```

---

## 🔹 Handling missing files

```python
try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
```

---



## 🧠 Key Takeaways

* Always validate **input, files, and CLI arguments**
* Use `try/except` for errors
* Use **specific exceptions**, not generic `except`
* Scripts should **fail gracefully** in the real world

---



✅ Day 6 teaches defensive scripting and prepares you for real-world automation and cybersecurity scripts.

# Day 3 – Functions & Script Structure

## 📌 What You Learn on Day 3

Day 3 focuses on **writing clean, reusable Python scripts** using functions and understanding how Python executes a script.

---

## 🔹 Functions in Python

A function is a reusable block of code that performs a specific task.

### Syntax

```python
def function_name(parameters):
    # code block
    return value
```

### Example

```python
def is_suspicious(count):
    return count > 5
```

This function:

* Takes `count` as input
* Returns `True` if the value is greater than 5

---

## 🔹 Using Functions with Loops

```python
dict_ip = {
    "192.168.100.1": 3,
    "192.168.100.2": 5,
    "192.168.100.3": 7,
    "192.168.100.4": 10
}

for ip, count in dict_ip.items():
    if is_suspicious(count):
        print(f"{ip} is suspicious")
```

Why this is good practice:

* Logic is separated
* Easy to change the condition later
* Code becomes readable and reusable

---

## 🔹 Script Entry Point

```python
if __name__ == "__main__":
    checking()
```

### Why this matters

* Ensures code runs **only when the file is executed directly**
* Prevents automatic execution when imported into another script

---



## 🧠 Key Takeaways

* Functions make scripts modular
* Logic should be separated from loops
* `__main__` protects execution flow
* This structure is used in real-world scripts

---



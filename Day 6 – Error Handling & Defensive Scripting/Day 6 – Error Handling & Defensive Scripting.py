import sys

# Get filename from command-line
try:
    filename = sys.argv[1]
except IndexError:
    print("Usage: python script.py <filename>")
    sys.exit()

# Read file safely
try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file was not found")

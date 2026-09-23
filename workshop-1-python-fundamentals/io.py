# Single string input
name = input("Enter your name: ").strip()

# Common in competitive programming
# Read line-by-line until EOF (Ctrl+D on Linux/macOS, Ctrl+Z on Windows)
import sys

print("Type lines (press Ctrl+D when done):")
for line in sys.stdin:
    line = line.strip()
    if line:
        print(f"Echo: {line}")

# File I/O: Iterates line-by-line (O(1) memory usage)
with open("example.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        # .rstrip("\n") removes trailing newlines without stripping spaces
        clean_line = line.rstrip("\r\n")
        print(f"Line {line_num}: {clean_line}")

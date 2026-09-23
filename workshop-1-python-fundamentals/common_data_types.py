import sys

# =====================================================================
# 1. NUMERIC TYPES: int, float, bool
# =====================================================================
print("--- 1. NUMERIC TYPES ---")

# int: Arbitrary-precision integers (do not overflow)
my_int = 42
huge_int = 10**100  # Automatically handled without overflow
print(f"int: {my_int}, bit_length: {my_int.bit_length()}")

# float: IEEE 754 double-precision floating-point (prone to rounding issues)
# 64 bits: first bit = sign; next 11 bits = exponent; next 52 bits = mantissa
# https://en.wikipedia.org/wiki/Double-precision_floating-point_format
my_float = 0.1 + 0.2
print(f"float: {my_float} (Notice: 0.1 + 0.2 == 0.3 is {my_float == 0.3})")

# bool: Subclass of int (True == 1, False == 0)
my_bool = True
print(f"bool is subclass of int: {isinstance(True, int)}")
print(f"Arithmetic with bool: True + True + False = {True + True + False}")

# =====================================================================
# 2. TEXT TYPE: str
# =====================================================================
print("\n--- 2. STRING (str) ---")

# str: Immutable sequence of Unicode characters
my_str = "  Python Data Types  "

# Methods return NEW strings; they cannot mutate in-place
print("Original:", repr(my_str))
print("Stripped & Lower:", repr(my_str.strip().lower()))
print("Split into list:", my_str.split())

try:
    my_str[0] = "J"  # TypeError: Strings are immutable
except TypeError as e:
    print("Immutability check:", e)

# =====================================================================
# 3. SEQUENCE TYPES: list, tuple, range
# =====================================================================
print("\n--- 3. SEQUENCES (list, tuple, range) ---")

# list: MUTABLE, ordered, allows duplicates
my_list = [3, 1, 2, 2]
my_list.append(4)  # Modifies in-place
my_list.sort()  # Modifies in-place
my_list[0] = 99  # Allowed because lists are mutable
print(f"list (mutable, ordered): {my_list}")

# tuple: IMMUTABLE, ordered, allows duplicates, hashable (can be dict key)
my_tuple = (3, 1, 2, 2)
# my_tuple[0] = 99 -> Raises TypeError
print(f"tuple (immutable, ordered): {my_tuple}")
print(f"Tuple unpack: a, b = (10, 20) -> a={10}, b={20}")

# range: IMMUTABLE, memory-efficient sequence of numbers generated on-demand
my_range = range(0, 1_000_000, 2)  # Even numbers up to 1 million
print(f"range object: {my_range}")
print(f"Memory of range(1_000_000): {sys.getsizeof(my_range)} bytes")
print(f"Memory of list(range(1_000_000)): {sys.getsizeof(list(my_range))} bytes")
print(f"Membership test in range: {999_998 in my_range}")

# =====================================================================
# 4. SET & MAPPING TYPES: set, dict
# =====================================================================
print("\n--- 4. SETS & DICTIONARIES ---")

# set: MUTABLE, UNORDERED (no indexing), UNIQUE elements only
my_set = {1, 2, 2, 3, 4}
print(f"set (auto-deduplicated): {my_set}")
my_set.add(5)

# Set algebra (intersections, unions, differences)
other_set = {4, 5, 6, 7}
print(f"Union (|): {my_set | other_set}")
print(f"Intersection (&): {my_set & other_set}")
print(f"Difference (-): {my_set - other_set}")

# dict: MUTABLE, key-value pairs (keys unique & hashable, preserves insertion order since Py 3.7)
my_dict = {"name": "Alice", "role": "Engineer"}
my_dict["age"] = 30  # Insert/Update

# Safe access with .get() avoids KeyError
print(f"dict lookup: name = {my_dict.get('name')}")
print(f"dict safe default: salary = {my_dict.get('salary', 'Not Disclosed')}")
print(f"Keys: {list(my_dict.keys())}, Values: {list(my_dict.values())}")

# =====================================================================
# 5. TRUTH VALUE TESTING (TRUTHY vs. FALSY)
# =====================================================================
print("\n--- 5. TRUTHY vs. FALSY VALUES ---")

# Every type in Python has a default "empty" or "zero" state that evaluates to False
falsy_values = [
    0,  # int
    0.0,  # float
    False,  # bool
    "",  # str
    [],  # list
    (),  # tuple
    range(0),  # range
    set(),  # set (note: {} creates an empty dict, not a set)
    {},  # dict
    None,  # NoneType
]

print("All the following evaluate to False:")
for val in falsy_values:
    print(f"  bool({repr(val):<10}) -> {bool(val)}")

print("\nNon-empty / Non-zero values evaluate to True:")
print(f"  bool([0])   -> {bool([0])}  (List is not empty, even though element is 0)")
print(f"  bool(' ')   -> {bool(' ')}  (Contains whitespace)")
print(f"  bool(-1)    -> {bool(-1)}   (Non-zero integer)")

# Idiomatic use in conditionals:
items = []
if not items:
    print("\nIdiomatic check: 'if not items:' detects an empty collection cleanly.")
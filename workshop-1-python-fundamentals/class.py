class Employee:

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        return f"{self.name} earns ${self.salary:,.2f}"

    # Static method: utility logic that doesn't need 'self' or 'cls'
    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        return salary >= 30_000


# Subclass inheriting from Employee
class Manager(Employee):

    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)  # Initialize parent attributes
        self.department = department

    # Overriding parent method
    def get_details(self) -> str:
        return f"{super().get_details()} (Dept: {self.department})"


# --- Usage ---

# 1. Calling the static method directly on the class (no instance needed)
print(Employee.is_valid_salary(25_000))  # Output: False
print(Employee.is_valid_salary(85_000))  # Output: True

# 2. Creating instances
emp = Employee("Alice", 50_000)
mgr = Manager("Bob", 95_000, "Engineering")

print(emp.get_details())  # Output: Alice earns $50,000.00
print(mgr.get_details())  # Output: Bob earns $95,000.00 (Dept: Engineering)


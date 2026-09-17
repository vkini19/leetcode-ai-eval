from code_executor import execute_solution


# Test 1: correct solution
correct_code = """
def add(a, b):
    return a + b
"""

result = execute_solution(
    correct_code,
    "add",
    (2, 3),
)

print("Correct code:")
print(result)


# Test 2: runtime error
bad_code = """
def add(a, b):
    return undefined_variable
"""

result = execute_solution(
    bad_code,
    "add",
    (2, 3),
)

print("\nRuntime error:")
print(result)


# Test 3: infinite loop
loop_code = """
def add(a, b):
    while True:
        pass
"""

result = execute_solution(
    loop_code,
    "add",
    (2, 3),
)

print("\nTimeout:")
print(result)
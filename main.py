import sys
import importlib

if len(sys.argv) < 2:
    print("Usage: python main.py <problem_prefix>")
    sys.exit(1)

prefix = sys.argv[1]  # e.g., "007"

# dynamically import module based on prefix
module_name = f"{prefix}_product_except_self"  # adjust pattern for each file
try:
    module = importlib.import_module(module_name)
except ModuleNotFoundError:
    print(f"No module found for prefix {prefix}")
    sys.exit(1)

# find class dynamically
solution_class = None
for name, obj in module.__dict__.items():
    if name.startswith(f"Solution{prefix}"):
        solution_class = obj
        break

if solution_class is None:
    print(f"No Solution class found in {module_name}")
    sys.exit(1)

# instantiate and run test
solution_instance = solution_class()
solution_instance.test()

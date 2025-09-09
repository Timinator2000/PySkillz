###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '----tools----'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the tools folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


class CodeAnalyzer(pyskillz_tools.TechioObject):

    def __init__(self):
        super().__init__(__file__)
    

    def run(self):
        self.print_analysis(self.code_analysis)


if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    analyzer.run()



"""

Perfect 👍 — we can structure the output in **two sections**:

1. **Summary** — just like before: grouped by type, counts of kept vs skipped.
2. **Detailed listing** — each statement with its line number, type, and snippet of code, along with whether it was counted or skipped.

Here’s the updated script:

```python
import ast
import sys
import textwrap
from collections import Counter

def analyze_code(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, filename)
    categories = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr):
            # Skip docstrings and string-only expressions
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                categories.append((node, "docstring/string literal", False))
                continue
        
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            categories.append((node, "import", False))
            continue
        
        if isinstance(node, ast.stmt):
            categories.append((node, type(node).__name__, True))
    
    # Count categories
    total_count = sum(1 for _, _, keep in categories if keep)
    kept = Counter(cat for _, cat, keep in categories if keep)
    skipped = Counter(cat for _, cat, keep in categories if not keep)

    # Print summary
    print(f"\nAnalysis of {filename}")
    print("=" * (12 + len(filename)))
    print("\nSummary of statement categories")
    print("--------------------------------")
    print("Statements kept (counted):")
    for cat, n in kept.items():
        print(f"  {cat}: {n}")
    if not kept:
        print("  (none)")

    print("\nStatements skipped:")
    for cat, n in skipped.items():
        print(f"  {cat}: {n}")
    if not skipped:
        print("  (none)")

    print("\nSummary totals:")
    print(f"  Total statements found: {len(categories)}")
    print(f"  Counted statements: {total_count}")
    print(f"  Skipped statements: {len(categories) - total_count}")
    print(f"\nFinal statement count: {total_count}\n")

    # Detailed breakdown
    print("Detailed statement breakdown")
    print("-----------------------------")
    for node, cat, keep in sorted(categories, key=lambda x: getattr(x[0], "lineno", 0)):
        lineno = getattr(node, "lineno", None)
        lineinfo = f"line {lineno}" if lineno is not None else "no line"
        status = "COUNTED" if keep else "SKIPPED"
        
        # Try to extract source line(s)
        snippet = ""
        if lineno is not None:
            try:
                snippet = source.splitlines()[lineno - 1].strip()
            except IndexError:
                snippet = "<source unavailable>"
        
        print(f"{lineinfo:>8} | {cat:<25} | {status:<7} | {snippet}")

    return total_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_code.py <filename>")
        sys.exit(1)
    analyze_code(sys.argv[1])
```

---

### Example Run

For the same `student.py`:

```python
import math

def square(x):
    "Return x squared"
    return x * x

print(square(5))
```

Output:

```
Analysis of student.py
======================

Summary of statement categories
--------------------------------
Statements kept (counted):
  FunctionDef: 1
  Return: 1
  Expr: 1

Statements skipped:
  import: 1
  docstring/string literal: 1

Summary totals:
  Total statements found: 5
  Counted statements: 3
  Skipped statements: 2

Final statement count: 3

Detailed statement breakdown
-----------------------------
   line 1 | import                   | SKIPPED | import math
   line 3 | FunctionDef              | COUNTED | def square(x):
   line 4 | docstring/string literal | SKIPPED | "Return x squared"
   line 5 | Return                   | COUNTED | return x * x
   line 7 | Expr                     | COUNTED | print(square(5))
```

---

👉 Do you want me to also group the **detailed breakdown** under “kept” vs “skipped” subsections for easier readability, or should it stay as one timeline ordered by line numbers?


"""
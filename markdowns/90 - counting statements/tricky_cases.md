Great question 👍

Yes — in Python’s AST, your example

```python
a_list = [[a, b*2, c*3] for a, b, c in [input().split() for _ in range(int(input()))]]
```

is **just one statement**: an `Assign` node (assignment statement).

Inside that statement:

* The right-hand side is a **list comprehension** → represented in the AST as a single `ListComp` expression.
* That `ListComp` contains:

  * An **outer comprehension** with target `a, b, c`.
  * An inner comprehension `[input().split() for _ in range(int(input()))]`.
* Each comprehension itself is not counted as a *statement*, but as an **expression node** inside the single assignment.

So if you run your analyzer, you’ll see only **one counted statement**:

```
line 1 | Assign | COUNTED | a_list = [[a, b*2, c*3] for a, b, c in [input().split() for _ in range(int(input()))]]
```

👉 If you wanted to *also count expressions inside comprehensions (or nested structures)*, you’d need to extend your logic beyond `ast.stmt` nodes and include certain `ast.expr` constructs.

Do you want me to show you how to modify your script so it can *optionally* break down comprehensions and count their internal operations too?


Excellent 😃 — let’s go deep into this. Your analyzer counts **AST `stmt` nodes** (except imports and docstrings). That means it aligns with Python’s grammar definition of a “statement.”



Here’s a **comprehensive guide** to “tricky” or non-obvious cases, and how they show up in the AST. I’ll break them into categories with examples.

---

## ✅ Simple Statements (straightforward, but worth confirming)

* **Assignments (`Assign`, `AnnAssign`, `AugAssign`)**

  ```python
  x = 5               # Assign → counts as 1
  y: int = 10         # AnnAssign → counts as 1
  z += 3              # AugAssign → counts as 1
  ```

  Even if the right-hand side is a complex comprehension, call, or lambda, it’s still *just one statement*.

* **Expressions (`Expr`)**

  ```python
  print("hi")   # Expr → counts as 1
  f(x, y, z)    # Expr → counts as 1
  ```

  ✅ You already skip string-only `Expr` nodes (docstrings), which is good.

---

## ⚡ Compound Statements (trickier, but still one node)

Each of these is a *single statement*, no matter how big the body is.

* **Function and Class definitions (`FunctionDef`, `AsyncFunctionDef`, `ClassDef`)**

  ```python
  def f(): return 1      # counts as 1
  async def g(): pass    # counts as 1
  class C: pass          # counts as 1
  ```

  * Bodies of functions/classes are *not counted here* — they are separate statements nested inside.

* **If statements (`If`)**

  ```python
  if x > 0: print("pos")    # counts as 1
  else: print("non-pos")    # still 1
  ```

  * Each `if`/`elif`/`else` chain is *one `If` node*.

* **Loops (`For`, `AsyncFor`, `While`)**

  ```python
  for i in range(10): pass     # counts as 1
  while cond: pass             # counts as 1
  ```

* **With statements (`With`, `AsyncWith`)**

  ```python
  with open("f.txt") as f: pass     # counts as 1
  async with lock: pass             # counts as 1
  ```

* **Try/Except/Finally (`Try`)**

  ```python
  try:
      risky()
  except ValueError:
      handle()
  finally:
      cleanup()
  ```

  → Whole `try` block (with all except/finally) is *one `Try` node*.

* **Match (structural pattern matching, Python 3.10+)**

  ```python
  match x:
      case 0: print("zero")
      case _: print("other")
  ```

  → Entire match block is *one `Match` node*.

---

## 🌀 Flow-control statements (all count as one each)

* `Return`, `Raise`, `Break`, `Continue`, `Pass`, `Yield` (inside functions).

  ```python
  return 5   # Return → counts as 1
  raise E()  # Raise → counts as 1
  break      # Break → counts as 1
  ```

  (They may *look* tiny but they are still separate statements.)

---

## 📝 Assignments with multiple targets

* **Tuple/List unpacking**

  ```python
  a, b = 1, 2   # still just 1 Assign
  ```
* **Chained assignment**

  ```python
  x = y = z = 0   # still 1 Assign
  ```

---

## ⚠️ Special/tricky cases

* **Decorators**

  ```python
  @deco
  def f(): pass
  ```

  → Still one `FunctionDef` node. Decorators live in `.decorator_list`, not as separate statements.

* **Lambda expressions**

  ```python
  f = lambda x: x+1
  ```

  → Counts as one `Assign`. The `lambda` is an `ast.Lambda` expression, *not* a statement.

* **Comprehensions**

  ```python
  [f(x) for x in data if x > 0]   # Expr → counts as 1 (if assigned or used)
  ```

  → No matter how nested or complex, it’s just part of one expression node.

* **F-strings, generators, ternary expressions**

  ```python
  x = f"hello {name}"             # Assign → 1
  y = (n for n in range(10))      # Assign → 1
  z = 1 if cond else 2            # Assign → 1
  ```

  → All are expressions inside a single `Assign`.

* **Imports** (you skip them already)

  ```python
  import math              # Import → skipped
  from os import path      # ImportFrom → skipped
  ```

* **Docstrings** (skipped already)

  ```python
  def f():
      "this is a docstring"
      return 1
  ```

  → The docstring is an `Expr` with `Constant(str)` → you skip it.

* **Assert**

  ```python
  assert x > 0   # Assert → counts as 1
  ```

* **Del**

  ```python
  del x          # Delete → counts as 1
  ```

* **Global / Nonlocal**

  ```python
  global x       # Global → counts as 1
  nonlocal y     # Nonlocal → counts as 1
  ```

---

## 🚫 Not counted (because they’re not statements)

* Expressions inside comprehensions, conditions, arguments, etc.
* Operators, arithmetic, comparisons.
* Keywords like `and`, `or`, `not`.
* Anything inside parentheses or curly braces, unless it forms its own statement.

---

## 🧾 Quick cheat sheet

| Syntax                      | AST Node Type       | Counted as statement? |
| --------------------------- | ------------------- | --------------------- |
| `x = 5`                     | Assign              | ✅ Yes                 |
| `x: int = 5`                | AnnAssign           | ✅ Yes                 |
| `x += 1`                    | AugAssign           | ✅ Yes                 |
| `print(x)`                  | Expr                | ✅ Yes                 |
| `"docstring"`               | Expr(Constant str)  | ❌ Skipped             |
| `import os`                 | Import              | ❌ Skipped             |
| `from os import path`       | ImportFrom          | ❌ Skipped             |
| `def f(): pass`             | FunctionDef         | ✅ Yes                 |
| `class C: pass`             | ClassDef            | ✅ Yes                 |
| `if cond: pass`             | If                  | ✅ Yes                 |
| `for x in items: pass`      | For                 | ✅ Yes                 |
| `while cond: pass`          | While               | ✅ Yes                 |
| `with open(...) as f: pass` | With                | ✅ Yes                 |
| `try: ... except: ...`      | Try                 | ✅ Yes                 |
| `match x: ...` (3.10+)      | Match               | ✅ Yes                 |
| `return x`                  | Return              | ✅ Yes                 |
| `raise E`                   | Raise               | ✅ Yes                 |
| `break / continue / pass`   | Break/Continue/Pass | ✅ Yes                 |
| `assert cond`               | Assert              | ✅ Yes                 |
| `del x`                     | Delete              | ✅ Yes                 |
| `global x` / `nonlocal x`   | Global/Nonlocal     | ✅ Yes                 |

---

👉 So in short: your analyzer correctly counts “syntactic statements.” The only things skipped are imports and docstrings, which is exactly what you wanted.

Would you like me to extend your **detailed breakdown** so that when it prints a statement, it also shows *why* it was classified as a statement (e.g., `Assign`, `If`, `Return`, etc.) and maybe even include the **AST node type description** from the cheat sheet above?



Perfect 👍 Let’s build a **clean, authoritative cheat sheet** that matches your analyzer’s behavior:

> **Rule of Thumb**
> Every compound statement (function, class, if, for, while, with, try, match) counts as **1 statement itself** **plus** all of the statements in its body.

---

# 🧾 Python Statement Counting Cheat Sheet (AST-based)

### ✅ Simple Statements (always count as 1)

| Example              | AST Node  | Count |
| -------------------- | --------- | ----- |
| `x = 5`              | Assign    | 1     |
| `x: int = 5`         | AnnAssign | 1     |
| `x += 1`             | AugAssign | 1     |
| `print(x)`           | Expr      | 1     |
| `return x`           | Return    | 1     |
| `raise ValueError()` | Raise     | 1     |
| `break`              | Break     | 1     |
| `continue`           | Continue  | 1     |
| `pass`               | Pass      | 1     |
| `assert x > 0`       | Assert    | 1     |
| `del x`              | Delete    | 1     |
| `global x`           | Global    | 1     |
| `nonlocal y`         | Nonlocal  | 1     |

---

### ⚡ Compound Statements (count + their body)

Each one counts as **1 for the compound itself** plus **each body statement**.

#### Functions

```python
def f(): return 1
```

* FunctionDef → 1
* Return → 1
* **Total = 2**

#### Classes

```python
class C:
    pass
```

* ClassDef → 1
* Pass → 1
* **Total = 2**

#### If / Elif / Else

```python
if x > 0: return 1
else: y = -1
```

* If → 1
* Return (in if) → 1
* Assign (in else) → 1
* **Total = 3**

#### Loops

```python
for i in range(3): print(i)
```

* For → 1
* Expr (print) → 1
* **Total = 2**

```python
while cond: pass
```

* While → 1
* Pass → 1
* **Total = 2**

#### With / Async With

```python
with open("f") as f: line = f.read()
```

* With → 1
* Assign → 1
* **Total = 2**

#### Try / Except / Finally

```python
try:
    x = 1
except:
    print("err")
finally:
    cleanup()
```

* Try → 1
* Assign (in try) → 1
* Expr (print) in except → 1
* Expr (cleanup) in finally → 1
* **Total = 4**

#### Match (3.10+)

```python
match x:
    case 0: return "zero"
    case _: return "other"
```

* Match → 1
* Return in case 0 → 1
* Return in case \_ → 1
* **Total = 3**

---

### 🚫 Skipped Statements (in your analyzer)

* **Imports** (`import ...`, `from ... import ...`) → skipped
* **Docstrings** (bare strings as `Expr` with `Constant(str)`) → skipped

---

### 📝 Summary of Counting Rules

* **Simple statement** → 1
* **Compound statement** → 1 **plus** all its body statements (recursively)
* **Imports & docstrings** → skipped
* **Expressions inside comprehensions, lambdas, or conditions** → not counted separately (part of their containing statement)

---

👉 This cheat sheet now exactly matches your analyzer’s behavior.

Would you like me to also create a **set of test code snippets + expected counts** (like a mini test suite) so you can verify your analyzer works correctly against all these tricky cases?

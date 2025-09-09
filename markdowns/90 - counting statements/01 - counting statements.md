# How We Count Your Lines of Code

In some exercises, there’s a **maximum number of statements** you’re allowed to use.
This isn’t to make life hard for you — it’s to encourage you to write code that is:

* **Concise** (short and to the point)
* **Elegant** (clear and clever)
* **Focused** (so the exercise can test the exact skill we want you to practice)

Think of it like solving a puzzle with just the right number of moves.

---

## What’s a “statement”?

A **statement** is a single instruction in Python.
Some examples of statements are:

* Assigning a variable:

  ```python
  x = 5
  ```
* Calling a function:

  ```python
  print("Hello")
  ```
* Starting a loop or conditional:

  ```python
  for i in range(3):
      ...
  ```

⚡ **Important:** You can put more than one statement on the same line with `;`,
but each one **still counts separately**.

---

## What doesn’t count?

Not everything you type is a statement. We **don’t count**:

* **Docstrings** — text in triple quotes `"""like this"""` at the top of a file, class, or function. These are just notes for people reading your code.
* **String-only expressions** — writing a string by itself, like `"hello"`.
* **Import statements** — they bring in modules but don’t count toward the “statements” limit.

---

## Examples

### Example 1: Assignment with a multiline string

```python
a = """
Hello
World
"""
```

✅ Counts as **1 statement** (an assignment).

### Example 2: Module docstring

```python
"""This exercise is about loops"""
```

🚫 Counts as **0 statements** (it’s just a description).

### Example 3: String-only expression

```python
"Temporary note"
```

🚫 Counts as **0 statements** (ignored).

### Example 4: Multiple prints on one line

```python
for c in "abc": print(c); print(c*2); print(c*3)
```

✅ Counts as **4 statements**:

* 1 `for` loop
* 3 `print` calls

On the next page, we'll test your understanding.
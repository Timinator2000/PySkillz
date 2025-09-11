# Math

Great idea 👍 — giving a new Python programmer math formulas to implement really shows whether they understand both math concepts and how to translate them into code. Below I’ll give you **20 progressively challenging formulas**, each of which can be directly coded in Python.

---

### Basic Arithmetic & Algebra

1. **Quadratic formula**:

   ```math
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   ```

2. **Distance between two points** $(x_1,y_1)$ and $(x_2,y_2)$:

   ```math
   d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
   ```

3. **Slope of a line through two points**:

   ```math
   m = \frac{y_2 - y_1}{x_2 - x_1}
   ```

4. **Midpoint of a line segment**:

   ```math
   M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)
   ```

5. **Circle area**:

   ```math
   A = \pi r^2
   ```

---math

### Geometry & Trigonometry

6. **Volume of a sphere**:

   ```math
   V = \frac{4}{3}\pi r^3
   ```

7. **Surface area of a cylinder**:

   ```math
   A = 2\pi r h + 2\pi r^2
   ```

8. **Pythagorean theorem**:

   ```math
   c = \sqrt{a^2 + b^2}
   ```

9. **Law of cosines**:

   ```math
   c^2 = a^2 + b^2 - 2ab\cos(\gamma)
   ```

10. **Convert degrees to radians**:

```math
\text{radians} = \frac{\pi}{180} \times \text{degrees}
```

---

### Sequences & Series

11. **Arithmetic series sum** (first $n$ terms):

```math
S_n = \frac{n}{2}(a_1 + a_n)
```

12. **Geometric series sum** (finite):

```math
S_n = a \frac{1-r^n}{1-r}
```

13. **Fibonacci recursion**:

```math
F(n) = F(n-1) + F(n-2)
```

14. **Factorial**:

```math
n! = n \times (n-1) \times (n-2) \times \cdots \times 1
```

15. **Binomial coefficient**:

```math
\binom{n}{k} = \frac{n!}{k!(n-k)!}
```

---

### Calculus & Higher Math

16. **Derivative of a polynomial** (e.g., power rule):

```math
\frac{d}{dx}(x^n) = nx^{n-1}
```

17. **Definite integral of a power**:

```math
\int_a^b x^n \, dx = \frac{b^{n+1} - a^{n+1}}{n+1}
```

18. **Taylor series expansion of $e^x$ (first n terms)**:

```math
e^x \approx \sum_{k=0}^n \frac{x^k}{k!}
```

19. **Newton-Raphson iteration** (root-finding):

```math
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
```

20. **Logarithm change of base**:

```math
\log_b a = \frac{\ln a}{\ln b}
```

---

👉 Each of these can be turned into a coding exercise — from straightforward computations (like circle area) to recursive/iterative problems (Fibonacci, Newton-Raphson), or working with loops/series (Taylor expansion).

Do you want me to **generate small Python function templates** for all 20, so you can hand them as exercises?



# Solutions

```python

# 9. Law of cosines
def law_of_cosines(a, b, gamma):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gamma))

# 11. Arithmetic series sum
def arithmetic_sum(n, a1, an):
    return n * (a1 + an) / 2

# 12. Geometric series sum
def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

# 13. Fibonacci recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 14. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# 15. Binomial coefficient
def binomial_coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

# 16. Polynomial derivative (power rule)
def derivative_power_rule(n):
    if n == 0:
        return 0
    return f"{n}*x^{n-1}"

# 17. Definite integral of power
def integral_power_rule(n, a, b):
    return (b**(n+1) - a**(n+1)) / (n+1)

# 18. Taylor series for e^x
def taylor_exp(x, n):
    total = 0
    for k in range(n+1):
        total += x**k / factorial(k)
    return total

# 19. Newton-Raphson iteration
def newton_raphson(f, f_prime, x0, iterations=10):
    x = x0
    for _ in range(iterations):
        x = x - f(x)/f_prime(x)
    return x

# 20. Logarithm change of base
def log_change_base(a, b):
    return math.log(a) / math.log(b)
```

---

✅ This set covers:

* Straight formulas (#1–12)
* Recursion (#13, #14)
* Combinatorics (#15)
* Symbolic-ish expression (#16)
* Calculus-based problems (#17–19)
* Logarithmic transformation (#20)

Do you want me to also **add test cases** (with example inputs + expected outputs) so a learner can run and verify each solution automatically?



# Test Cases

Perfect 👍 — I’ll add **simple test cases** for each function so a new programmer can immediately run and check if their code works.
I’ll use `print()` style tests with expected answers in comments.

---

```python
import math

# ---------- FUNCTIONS (from previous solution) ----------

def quadratic_roots(a, b, c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return None
    sqrt_disc = math.sqrt(disc)
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)
    return (x1, x2)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def circle_area(r):
    return math.pi * r**2

def sphere_volume(r):
    return (4/3) * math.pi * r**3

def cylinder_surface_area(r, h):
    return 2*math.pi*r*h + 2*math.pi*r**2

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def law_of_cosines(a, b, gamma):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gamma))

def deg_to_rad(deg):
    return deg * math.pi / 180

def arithmetic_sum(n, a1, an):
    return n * (a1 + an) / 2

def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def binomial_coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def derivative_power_rule(n):
    if n == 0:
        return 0
    return f"{n}*x^{n-1}"

def integral_power_rule(n, a, b):
    return (b**(n+1) - a**(n+1)) / (n+1)

def taylor_exp(x, n):
    total = 0
    for k in range(n+1):
        total += x**k / factorial(k)
    return total

def newton_raphson(f, f_prime, x0, iterations=10):
    x = x0
    for _ in range(iterations):
        x = x - f(x)/f_prime(x)
    return x

def log_change_base(a, b):
    return math.log(a) / math.log(b)


# ---------- TEST CASES ----------

print("1:", quadratic_roots(1, -3, 2))         # (2.0, 1.0)
print("2:", distance(0, 0, 3, 4))              # 5.0
print("3:", slope(0, 0, 2, 2))                 # 1.0
print("4:", midpoint(0, 0, 4, 4))              # (2.0, 2.0)
print("5:", circle_area(3))                    # 28.274...
print("6:", sphere_volume(1))                  # 4.188...
print("7:", cylinder_surface_area(2, 5))       # 87.964...
print("8:", hypotenuse(3, 4))                  # 5.0
print("9:", law_of_cosines(3, 4, math.pi/2))   # 5.0
print("10:", deg_to_rad(180))                  # 3.14159...
print("11:", arithmetic_sum(10, 1, 10))        # 55.0
print("12:", geometric_sum(1, 2, 4))           # 15.0
print("13:", fibonacci(10))                    # 55
print("14:", factorial(5))                     # 120
print("15:", binomial_coeff(5, 2))             # 10
print("16:", derivative_power_rule(3))         # "3*x^2"
print("17:", integral_power_rule(2, 0, 3))     # 9.0
print("18:", taylor_exp(1, 5))                 # ~2.7167 (approx e)
print("19:", newton_raphson(lambda x: x**2-2, lambda x: 2*x, 1))  # ~1.414...
print("20:", log_change_base(8, 2))            # 3.0
```

---

✅ With this, you’ve got:

* **20 exercises**
* **Solutions**
* **Test cases** (so learners can check correctness automatically)

Would you like me to also **convert these tests into `assert` statements** instead of `print()` so they behave more like automated unit tests?

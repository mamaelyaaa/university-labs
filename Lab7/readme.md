# How to use?

1. Init your `function`, `df` and `d2f`

```python
def f(x: float) -> float:
    return x ** 2 + 1 / atan(x)


def df(x: float) -> float:
    return 2 * x - 1 / ((x ** 2 + 1) * atan(x) ** 2)


def d2f(x: float) -> float:
    return 2 + 2 * x * atan(x) + 2 / ((x ** 4 + 2 * x ** 2 + 1) * atan(x) ** 3)
```
2. Init your borders and eps:

```python
A: float = 0
B: float = 2

E: float = 0.005
```

3. If you need to determine the accuracy of these methods, find the points of maximum or minimum:

```python
answer: float = 0.757
```

## Problem with `ZeroDivisionError`

For the very first point **x0** we take either the **beginning A** or the **end B**. This depends on the increase or decrease of the function, as well as in which direction the function is convex.

1. In `method_polyline()` 

Line 57
```text
for x in range(B, A, -1):

# for x in range(A, B):
```

Lines 60-61

```text
x: float = 1 / (2 * L) * (f(B) + L * (A + B))
p: float = (f(B) + L * (A - B)) / 2

# x: float = 1 / (2 * L) * (f(a) - f(B) + L * (A + B))
# p: float = (f(a) + f(B) + L * (A - B)) / 2
```

2. In `method_tangents()`

Line 82

```text
x0 = B
# x0 = A
```

3. In `method_Newton()`

Line 94

```text
x0 = B
# x0 = A
```
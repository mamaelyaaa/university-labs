# How to use?

It is necessary to indicate

1. The _left_ and _right_ boundaries of the integral
```Python
A: float = -0.4  # Left border
B: float = 0.8  # Right border
```

2. The integrand in the function F

```Python
def f(x: float) -> float:
    return x ** 2 / (4 * x ** 3 + 1)
```
3. Calculate the integral (to compare methods)

```Python
expectedIntegralRes: float = 0.117517
```
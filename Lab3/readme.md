# How to use

You need to specify:

1. `x_approximate_val`

```python
x_approximate_val: float = 5.5
```

2. `x0` and `y0`

```python
x: list[float] = [1.0]  # x0
y: list[float] = [1.0]  # y0
```

3. Your **function** and **df**:

```python
def f(x: float, y: float) -> float:
    return y / x - (2 * x) / x ** 2


def f1(x: float, y: float) -> float:
    return (f(x, y) * x - (y - 2)) / x ** 2
```

4. Your steps (unnecessary):

```python
step: list[float] = [0.5, 0.1, 0.01]
```

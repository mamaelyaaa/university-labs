# How to use

Function `generation` creates an array[`N`] of random values

If you need to sort a specific array, you need to **initialize** `arr`:

```python
arr: list = []
```

Accordingly, remove or comment out these lines

```python
with open('input.txt', 'r') as file_input:
    arr: list[int] = list(map(int, file_input.readline().split()))
```

Finally, you'll get running time of different algorithms
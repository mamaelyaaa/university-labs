# How to use?

First of all, you need to fill `input_data.txt` with your system of linear equations like that: (_First line no need_)

```text
#                [A]                   [B]
-34.0  -0.34   0.28   0.31  -0.79    1446.313
-0.05   11.0   0.86   0.85  -0.10   -102.487
 0.63   0.47  -90.0   0.74  -0.06    3885.689
 0.22   0.62  -0.04  -54.0   0.84    2002.667
 0.31   0.85  -0.95  -0.22  -720.0  -1062.924
```

This is enough if you need answers for your systems of linear equations, but if you need to compare answers with real ones
you need to calculate them, fill hashmap `EXP_ANS` and program will give `max error` 

```python
EXP_ANS: dict = {'a': -43.24231639,
                 'b': -3.197390354,
                 'c': -43.80095293,
                 'd': -37.24317186,
                 'e': 1.523063199}
```

```text
Method Gauss:         a = ... b = ... c = ... d = ... e = ...
max error =  0.0000000013
```




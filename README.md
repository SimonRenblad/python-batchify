# python-batchify
Small module for converting a list to a nested list with elements as lists of a certain batch size

## Documentation

### Import Module

```python
import batchify
```

### Batchify

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = batchify.batchify(my_list, 3)
print(my_list)
```
Output:
```python
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

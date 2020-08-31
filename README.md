# python-batchify
Small module for converting a list to a nested list with elements as lists of a certain batch size

## Documentation

### Import Module

```python
import batchify
```

### batchify

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = batchify.batchify(my_list, 3)
print(my_list)
```
Output:
```python
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

### unbatchify

```python
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
my_list = batchify.unbatchify(my_list)
print(my_list)
```
Output:
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### is_batched

```python
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
print(batchify.is_batched(my_list))

my_list = [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10]]
print(batchify.is_batched(my_list))
```
Output:
```python
True
False
```

# Python solutions

> Problems solved using Python 3.7.3

> All modules adhere to pep8 standard and no additional dependencies are required

## Table of contents

1. [`is_none_or_empty`](#is_none_or_empty)
1. [`get_positive_divisors`](#get_pos_divs)
1. [`get_area_of_triangle`](#get_area_of_triangle)
1. [`get_common_nums`](#get_common_nums)

## `is_none_or_empty`

> This module returns True if the input is None or empty, otherwise it returns False

### Running the code

To run the code:

```shell
# Pass in the value as command-line arguments. For the None test case, do not pass an argument
python is-none-or-empty/main.py
python is-none-or-empty/main.py 'a'
```

### Running the tests

To run the tests:

```shell
python is-none-or-empty/tests.py
```

## `get_pos_divs`

> This module returns a collection of integers that are divisors of the positive input integer

### Running the code

To run the code:

```shell
# Pass in the value as a command-line argument
python get-positive-divisors/main.py 42
```

### Running the tests

To run the tests:

```shell
python get-positive-divisors/tests.py
```

## `get_area_of_triangle`

> This module calculates the area of a triangle when given the length of three sides. The calculation is done using Heron's formula. The triangle must be valid and all sides must be positive or an InvalidTriangle exception will be thrown

### Running the code

To run the code:

```shell
# Pass in the triangle dimensions as command-line arguments
python get-area-of-triangle/main.py 3 4 5
```

### Running the tests

To run the tests:

```shell
python get-area-of-triangle/tests.py
```

## `get_common_nums`

> given a list of integers, this module returns the most common numbers that exist in the list

### Running the code

To run the code:

```shell
# Pass in the command-line list as a string
python get-common-nums/main.py 5 4 3 2 4 5 1 6 1 2 5 4
```

### Running the tests

To run the tests:

```shell
python get-common-nums/tests.py
```

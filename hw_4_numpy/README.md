# README file for HW #4

This script contains following functions:

- `matrix_multiplication` - takes two matrices and returns matrix multiplication product
- `multiplication_check` - takes list of matrices (2d-arrays) and returns `True` or `False` depending on their ability to be multiplied
- `multiply_matrices` - takes in list of matrices and multiples them one by one and returns `None` if it's inmpossible to multiply
- `compute_2d_distance` - computes distance between two pairs of given coordinates (1-dimensional arrays)
- `compute_multidimensional_distance` - basically does the same for 1-dimensional arrays with any number of elements
- `compute_pair_distances` - takes in 2d array where every row is an observation and column is a feature and computed matrix of paired distances

This script also contains three of my favourite arrays (uncomment line in main to print to console).

## Requirements

This script requires [`numpy`](https://numpy.org/). It was tested on `Ubuntu 20.04` only with `numpy` version 1.23.4. You can easily install it via [venv](https://docs.python.org/3/library/venv.html). After creation of virtual environment and its activation all required dependencies can be installed via the following command:
`pip3 install -r /path/to/requirements.txt`. `requirements.txt` can be found in the current repo as well.


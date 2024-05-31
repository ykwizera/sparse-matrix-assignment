
# Sparse Matrix Operations

This project provides a Python implementation for performing basic operations (addition, subtraction, and multiplication) on sparse matrices. Sparse matrices are matrices in which most of the elements are zero. The implementation reads matrices from files, performs operations, and writes the results to new files.

## Project Structure

```
.
├── sample_inputs
│   ├── matrixA.txt
│   └── matrixB.txt
├── results
│   ├── sum.txt
│   ├── difference.txt
│   └── product.txt
├── sparse_matrix.py
└── README.md
```

- `sample_inputs/` : Directory containing the input matrix files.
- `results/` : Directory where the result files will be saved.
- `sparse_matrix.py` : Python script containing the implementation of sparse matrix operations.
- `README.md` : This README file.

## Prerequisites

- Python 3.6 or higher.

## Usage

### Input File Format

Input files should be located in the `sample_inputs/` directory and should follow this format:

```
numRows=<number_of_rows>
numCols=<number_of_columns>
(row, col, value)
(row, col, value)
...
```

Example:
```
numRows=3
numCols=3
(0, 0, 5)
(1, 1, 8)
(2, 2, 3)
```

### Running the Script

1. Place your input files (`matrixA.txt` and `matrixB.txt`) in the `sample_inputs/` directory.
2. Run the script:

```bash
python sparse_matrix.py
```

The script will read the matrices from the input files, perform addition, subtraction, and multiplication, and save the results in the `results/` directory.

## Output

The result files will be saved in the `results/` directory with the following names:
- `sum.txt` : Contains the result of matrix addition.
- `difference.txt` : Contains the result of matrix subtraction.
- `product.txt` : Contains the result of matrix multiplication.

Each result file follows the same format as the input files.

## Error Handling

- If the input files are not in the correct format, the script will raise a `ValueError` with a message indicating the issue.
- If matrix dimensions do not match for the operation, a `ValueError` will be raised.

## Contributing

Contributions are welcome! Please create an issue or pull request for any enhancements or bug fixes.

## authors
Yvette Kwizera

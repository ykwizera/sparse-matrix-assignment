import os
import re

class SparseMatrix:
    def __init__(self, filePath=None, numRows=None, numCols=None):
        if filePath:
            self.read_from_file(filePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.elements = {}

    def read_from_file(self, filePath):
        with open(filePath, 'r') as file:
            lines = file.readlines()
            
            if len(lines) < 2:
                raise ValueError("Input file has wrong format")

            self.numRows = int(lines[0].split('=')[1].strip())
            self.numCols = int(lines[1].split('=')[1].strip())
            self.elements = {}

            for line in lines[2:]:
                line = line.strip()
                if line.startswith('(') and line.endswith(')'):
                    elements = line[1:-1].split(',')
                    if len(elements) != 3:
                        raise ValueError("Input file has wrong format")
                    row, col, value = map(int, elements)
                    self.set_element(row, col, value)
                else:
                    raise ValueError("Input file has wrong format")

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        if value == 0:
            if (row, col) in self.elements:
                del self.elements[(row, col)]
        else:
            self.elements[(row, col)] = value

    def add(self, matrix):
        if self.numRows != matrix.numRows or self.numCols != matrix.numCols:
            raise ValueError("Matrix dimensions must match for addition")

        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)

        for (row, col), value in self.elements.items():
            result.set_element(row, col, value + matrix.get_element(row, col))

        for (row, col), value in matrix.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, value)

        return result

    def subtract(self, matrix):
        if self.numRows != matrix.numRows or self.numCols != matrix.numCols:
            raise ValueError("Matrix dimensions must match for subtraction")

        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)

        for (row, col), value in self.elements.items():
            result.set_element(row, col, value - matrix.get_element(row, col))

        for (row, col), value in matrix.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, -value)

        return result

    def multiply(self, matrix):
        if self.numCols != matrix.numRows:
            raise ValueError("Matrix dimensions must match for multiplication")

        result = SparseMatrix(numRows=self.numRows, numCols=matrix.numCols)

        for (rowA, colA), valueA in self.elements.items():
            for colB in range(matrix.numCols):
                valueB = matrix.get_element(colA, colB)
                if valueB != 0:
                    result.set_element(rowA, colB, result.get_element(rowA, colB) + valueA * valueB)

        return result

    def __str__(self):
        result = f"rows={self.numRows}\ncols={self.numCols}\n"
        for (row, col), value in self.elements.items():
            result += f"({row}, {col}, {value})\n"
        return result

def write_matrix_to_file(matrix, filePath):
    with open(filePath, 'w') as file:
        file.write(str(matrix))

def main():
    try:
        input_dir = "./sample_inputs/"
        output_dir = "./sample_results/"
        os.makedirs(output_dir, exist_ok=True)

        matrixA_path = os.path.join(input_dir, "matrix1.txt")
        matrixB_path = os.path.join(input_dir, "matrix2.txt")

        matrixA = SparseMatrix(matrixA_path)
        matrixB = SparseMatrix(matrixB_path)

        sum_matrix = matrixA.add(matrixB)
        diff_matrix = matrixA.subtract(matrixB)
        prod_matrix = matrixA.multiply(matrixB)

        write_matrix_to_file(sum_matrix, os.path.join(output_dir, "sum.txt"))
        write_matrix_to_file(diff_matrix, os.path.join(output_dir, "difference.txt"))
        write_matrix_to_file(prod_matrix, os.path.join(output_dir, "product.txt"))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

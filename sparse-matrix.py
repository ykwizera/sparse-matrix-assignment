import os
import re

class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=0, numCols=0):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = {}
        
        if matrixFilePath:
            self.read_from_file(matrixFilePath)

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def read_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            
            self.numRows = int(lines[0].split('=')[1].strip())
            self.numCols = int(lines[1].split('=')[1].strip())
            
            for line in lines[2:]:
                line = line.strip()
                if not line:
                    continue
                
                if not re.match(r'^\(\d+,\s*\d+,\s*-?\d+\)$', line):
                    raise ValueError("Input file has wrong format")

                line = line[1:-1]  # Remove parentheses
                row, col, value = map(int, line.split(','))
                self.set_element(row, col, value)

    def __add__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) + value)
        return result

    def __sub__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) - value)
        return result

    def __mul__(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions do not match for multiplication")

        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (row1, col1), value1 in self.elements.items():
            for (row2, col2), value2 in other.elements.items():
                if col1 == row2:
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)
        return result

    def print(self):
        for (row, col), value in self.elements.items():
            print(f"({row}, {col}, {value})")

# def main():
#     try:
#         base_dir = "/sample_inputs/"
#         matrix1_path = os.path.join(base_dir, "easy_sample_01_1.txt")
#         matrix2_path = os.path.join(base_dir, "easy_sample_01_2.txt")

#         mat1 = SparseMatrix(matrix1_path)
#         mat2 = SparseMatrix(matrix2_path)

#         print("Matrix 1:")
#         mat1.print()
#         print("\nMatrix 2:")
#         mat2.print()

#         print("\nSum:")
#         sum_matrix = mat1 + mat2
#         sum_matrix.print()

#         print("\nDifference:")
#         diff_matrix = mat1 - mat2
#         diff_matrix.print()

#         print("\nProduct:")
#         product_matrix = mat1 * mat2
#         product_matrix.print()

#     except Exception as e:
#         print(e)

# if __name__ == "__main__":
#     main()

def main():
    try:
        base_dir = "/sample_inputs/"
        results_dir = "/results/"
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        matrix1_path = os.path.join(base_dir, "easy_sample_01_1.txt")
        matrix2_path = os.path.join(base_dir, "easy_sample_01_2.txt")

        mat1 = SparseMatrix(matrix1_path)
        mat2 = SparseMatrix(matrix2_path)

        print("Matrix 1:")
        with open(os.path.join(results_dir, "matrix1.txt"), "w") as f:
            for (row, col), value in mat1.elements.items():
                f.write(f"({row}, {col}, {value})\n")
        mat1.print()

        print("\nMatrix 2:")
        with open(os.path.join(results_dir, "matrix2.txt"), "w") as f:
            for (row, col), value in mat2.elements.items():
                f.write(f"({row}, {col}, {value})\n")
        mat2.print()

        print("\nSum:")
        sum_matrix = mat1 + mat2
        with open(os.path.join(results_dir, "sum.txt"), "w") as f:
            for (row, col), value in sum_matrix.elements.items():
                f.write(f"({row}, {col}, {value})\n")
        sum_matrix.print()

        print("\nDifference:")
        diff_matrix = mat1 - mat2
        with open(os.path.join(results_dir, "diff.txt"), "w") as f:
            for (row, col), value in diff_matrix.elements.items():
                f.write(f"({row}, {col}, {value})\n")
        diff_matrix.print()

        print("\nProduct:")
        product_matrix = mat1 * mat2
        with open(os.path.join(results_dir, "product.txt"), "w") as f:
            for (row, col), value in product_matrix.elements.items():
                f.write(f"({row}, {col}, {value})\n")
        product_matrix.print()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
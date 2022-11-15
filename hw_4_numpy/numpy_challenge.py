import numpy as np

if __name__ == "__main__":
    first_array = np.zeros(10) 
    second_array = np.array([['Argentina', 'Jamaica'], [5, 0]]) 
    third_arrray = np.arange(18) 

    #print(first_array, second_array, third_arrray, sep = '\n')



def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def multiplication_check(matrix_lst): # so that multiplication will only work on 2d arrays
    matrix_product = np.array(matrix_lst[0].shape)
    can_multiply = True
    for m in matrix_lst:
        if m.ndim != 2:
            can_multiply = False
            break
        can_multiply = can_multiply and (matrix_product.shape[1] == m.shape[0])
    return can_multiply

def multiply_matrices(matrix_lst):
    if multiplication_check(matrix_lst):
        matrix_product = np.array(matrix_lst[0].shape)
        for m in matrix_lst:
            matrix_product = matrix_multiplication(matrix_product, m)
    return matrix_product

def compute_2d_distance(m1, m2):
    return np.linalg.norm(m1 - m2)
            
def compute_multidimensional_distance(m1, m2):
    return np.linalg.norm(m1 - m2)

#def compute_pair_distances(array):


matrix_lst = [np.array([0, 1, 3]), np.array([[1, 1], [1, 1]])]
print(multiplication_check(matrix_lst))

matrix_lst = [np.array([[4, 2], [9, 0]]), np.array([[3, 1], [-3, 4]])]
print(multiplication_check(matrix_lst))

print(multiply_matrices(matrix_lst))

print(matrix_multiplication(matrix_lst[0], matrix_lst[1]))
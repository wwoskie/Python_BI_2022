import numpy as np

if __name__ == "__main__":
    first_array = np.zeros(10) 
    second_array = np.array([['Argentina', 'Jamaica'], [5, 0]]) 
    third_arrray = np.arange(18) 

    #print(first_array, second_array, third_arrray, sep = '\n')



def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def multiplication_check(matrix_lst): 
    prev_matrix = matrix_lst[0]
    can_multiply = True
    for m in matrix_lst[1:]:
        '''
        multiplication check would fail for single matrices 
        and if array is not a matrix (just an array)
        also it would leave loop if can_multyply is already False
        '''
        if m.ndim != 2  or prev_matrix.ndim != 2 or len(matrix_lst) < 2 or can_multiply == False:
            can_multiply = False
            break
        can_multiply = can_multiply and (prev_matrix.shape[1] == m.shape[0])
        prev_matrix = m
    return can_multiply

def multiply_matrices(matrix_lst):
    if multiplication_check(matrix_lst):
        matrix_product = matrix_multiplication(matrix_lst[0], matrix_lst[1])
        if len(matrix_lst) > 2: # would go here only if matrix_lst is longer than 2
            for m in matrix_lst[2:]:
                matrix_product = matrix_multiplication(matrix_product, m)
    else:
        matrix_product = None
    return matrix_product

def compute_2d_distance(m1, m2):
    return np.linalg.norm(m1 - m2)
            
def compute_multidimensional_distance(m1, m2):
    return np.linalg.norm(m1 - m2)

def compute_pair_distances(array):
    return np.linalg.norm(array[:, None, :] - array[None, :, :], axis=-1)
import numpy as np

if __name__ == "__main__":
    first_array = np.zeros(10) # first array cause i just linda like zeros they are beautiful
    second_array = np.array([['Argentina', 'Jamaica'], [5, 0]]) # the most painful one
    third_arrray = np.arange(18) # cause i still fill like 17 though people think i'm already 18

    #print(first_array, second_array, third_arrray, sep = '\n')



def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def multiplication_check(matrix_lst):
    matrix_product = np.ones(np.shape(matrix_lst[0]))
    can_multiply = True
    for m in matrix_lst:
        can_multiply = can_multiply and (matrix_product.shape[0] == m.shape[1])
    return can_multiply

def multiply_matrices(matrix_lst):
    matrix_product = np.ones(np.shape(matrix_lst[0]))
    can_multiply = True
    for m in matrix_lst:
        if can_multiply and multiplication_check(list(matrix_product, m)):
            matrix_product = matrix_multiplication(matrix_product, m)
        else:
            matrix_product = None
            break
    return matrix_product

def compute_2d_distance(m1, m2):
    return np.linalg.norm(m1 - m2)
            
def compute_multidimensional_distance(m1, m2):
    return np.linalg.norm(m1 - m2)

def compute_pair_distances(array):


matrix_lst = [np.array([0, 1, 3]), np.array([[1, 1], [1, 1]])]
print(multiplication_check(matrix_lst))

matrix_lst = [np.array([[0, 1], [0, 0]]), np.array([[1, 1], [1, 1]])]
print(multiplication_check(matrix_lst))
#!/usr/bin/env python3
import numpy as np

'''
Why array[i] = list is okay ?
'''
def get_row(row_n):
    #   turn input into list(int)
    mat_ls = [float(i) for i in (input("row {} of the matrix, in the form of 0,0,0 :".format(row_n)).split(","))]
    return mat_ls


def mat_tp(dim, mat_0):    #transpose matrix
    dim_rev = [0,0]
    dim_rev[0] = dim[1]
    dim_rev[1] = dim[0]
    temp_mat = np.zeros(dim_rev)    # zeros array
    for i in range(dim[0]):
        for j in range(dim[1]):
            temp_mat[j][i] = mat_0[i][j]
    return temp_mat

def main():
    dim = int(input("dimension of the square matrix:")) #get dimension of the matrix
    mat_first = np.zeros((dim,dim))  # square matrix
    for x in range(dim):
        mat_first[x] = get_row(x+1)

    result = np.dot(mat_first,mat_first.transpose())
    
    print(result)


# in python3, if statement can be ignored
if __name__ == '__main__':
    main()

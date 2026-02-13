import numpy as np

def standardize_rows(data, mean, std):
    d = []
    
    for r in data:
        s_r = [(r[i] - mean[i]) / std[i] for i in range(len(r))]
        # Append the standardized row to the result list
        d.append(s_r)
    
    return np.array(d)


# data = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# mean = [0.5, 1, 3]
# std = [1, 2, 3]
# print(standardize_rows(data, mean, std))

def outer(x, y):
    outer_product = []
    
    for i in range(len(x)):
        row = []

        for j in range(len(y)):
            product = x[i] * y[j]
            row.append(product)

        outer_product.append(row)
    
    return np.array(outer_product)

# x = [1, 2]
# y = [3, 4, 5]

# print(outer(x, y))

def distmat_1d(x, y):
    distance_matrix = [[abs(x_i - y_j) for y_j in y] for x_i in x]
    return np.array(distance_matrix)

# Example usage
x = [1, 2]
y = [3, 0.5, 1]
 
print(distmat_1d(x, y))
import sys
import numpy as np

# # one loop
# def distance_matrix(p1, p2):
#     p1, p2 = np.radians(p1), np.radians(p2)
#     D = np.zeros((p1.shape[0], p2.shape[0]))

#     for i in range(p1.shape[0]):
#         lat1, lon1 = p1[i, 0], p1[i, 1]
#         lat2, lon2 = p2[:, 0], p2[:, 1]

#         dlat = lat1 - lat2
#         dlon = lon1 - lon2

#         a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
#         c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

#         D[i, :] = 6371 * c  # Earth radius in km

#     return D

# No loops
def distance_matrix(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)

    lat1, lon1 = p1[:, 0][:, np.newaxis], p1[:, 1][:, np.newaxis]
    lat2, lon2 = p2[:, 0], p2[:, 1]

    dlat = lat1 - lat2
    dlon = lon1 - lon2

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    D = 6371 * c  # Earth radius in km
    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix(points, points)
stats = distance_stats(D)
print(stats)

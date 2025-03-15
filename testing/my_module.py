import numpy as np

def normalize_data(data):

    data = np.array(data)

    mean = np.mean(data, axis=0)

    std = np.std(data, axis=0)

    normalized_data = (data - mean) / std

    return normalized_data.tolist()

if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(normalize_data(data))
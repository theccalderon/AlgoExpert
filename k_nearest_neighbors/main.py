# This is a sample Python script.
import itertools


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def euclidean_distance(X, Y):
    new_list = [0 for x in X]
    for i in range(len(X)):
        new_list[i] = (X[i] - Y[i]) ** 2
    return sum(new_list) ** 0.5


# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    # Write your code here.
    pass


def find_k_nearest_neighbors(examples, features, k):
    distances = dict.fromkeys(examples.keys, None)
    for pid, example_features in examples.items():
        distances[pid] = euclidean_distance(features, example_features)
    sorted_distances = sorted(distances)
    return dict(itertools.islice(sorted_distances.items(), k)).keys()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random
import numpy as np

#
# K-means clustering algorithm implementation
# By: Timothy Gaweco
#

# Example data
points = [(1,2),(3,5),(5,7),(10,5),(15,7),(20,10),(65,12),(56,15),(4,5)]

# Distance function (Eucledian distance)
def distance(point1, point2):
    dist = 0
    dim = len(point1)

    for d in range(dim):
        dist += (point2[d] - point1[d]) ** 2

    return dist

# K-means function
def kmeans(points, k):

    # Find max and min in each dimension
    maximum = [0 for i in range(len(points[0]))]
    minimum = [100 for i in range(len(points[0]))]

    for p in points:
        pos = 0
        for dim in p:
            if dim > maximum[pos]:
                maximum[pos] = dim
            if dim < minimum[pos]:
                minimum[pos] = dim
            pos += 1

    print maximum
    print minimum

    # Randomly assign k cluster centroids
    centroids = []
    centroid = ()
    for i in range(k):
        for j in range(len(maximum)):
            number = random.random() * (maximum[j] - minimum[j]) + minimum[j]
            centroid += (number,)
        centroids.append((centroid, i)) # add centroid number
        centroid = ()

    print centroids

    clusters = [ [] for i in range(k)]
    min_dist = 0
    centroid_num = 0
    # Assign each point to closest centroid
    for p in points:
        # Find closest centroid
        for c in centroids:
            dist = distance(p, c)

            if dist < min_dist:
                min_dist = dist
                centroid_num = c[1]

        clusters[centroid_num-1].append(p)

    # Compute new average of points assigned to cluster k, change centroids
    points_in_cluster = []
    new_centroids = []
    for cluster in clusters:
        for p in cluster:
            points_in_cluster.append(p[0])

        dim_points = []
        for dim in points[0]:
            for points in points_in_cluster:
                dim_points.append(points[dim])

            np.average(dim_points)

        points_in_cluster = []

    return clusters

if __name__ == '__main__':
    print kmeans(points,2)
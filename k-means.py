import random

#
# K-means clustering algorithm implementation
# By: Timothy Gaweco
#

# Example data
points = [(1,2),(3,5),(5,7),(10,5),(15,7),(20,10),(65,12),(56,15),(4,5)]

# Distance function
def distance(point1, point2):
    dist = 0



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
        centroids.append(centroid)
        centroid = ()

    print centroids

    clusters = [(1000000,'Cluster 1') for i in range(len(points))]
    pos = 0
    # Assign each point to closest centroid
    for p in points:
        for c in centroids:
            dist = distance(p, c)

            if dist < clusters[pos][0]:
                clusters[pos] = (dist, ) #add cluster number?


    # Compute new average of points assigned to cluster k


    return clusters


if __name__ == '__main__':
    print kmeans(points,2)
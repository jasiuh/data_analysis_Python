# Assign_to_clusters
# Take inputs: data, clusters, centroids, and point_assignments
# This function will go though each point and index that point in
# the data and find the closest centroid.
# Then append that point to the list of points for that cluster in the
# clusters variable
def assign_to_clusters(data, clusters, centroids, point_assignments):
    point_assignments = []    
    for count, elems in enumerate(data):
        dif = 10000
        j = 0
        for k in range(len(centroids)):
            dif1 = abs(elems - centroids[k])
            if dif1 < dif:
                dif = dif1
                j = k
        clusters[j].append(elems)
        point_assignments.append(tuple((data[count], j)))
    return point_assignments


# Update_centroids
# Take inputs:  clusters, centroids, and k.
# Go though each list contained in clusters variable and recompute the
# centroid by averaging over all the points in that list.
# Then update the corresponding centroids value.
def update_centroids(clusters, centroids, k):
    for x in range(k):
        average = 0
        for i in range(len(clusters[x])):
            average = average + clusters[x][i]
        average = average/len(clusters[x])
        centroids[x] = average
    return centroids


def main():
    # Ask for file name and output file name
    # MAKE SURE INPUT FILE IS IN SAME DIRECTORY AS SOURCE CODE
    input_file = raw_input("Enter the name of the input file: ")
    output_file = raw_input("Enter the name of the output file: ")
    # Prompt for clusters K
    k = int(raw_input("Enter the number of clusters: "))  # Clusters = 5

    # Open file and strip all lines of ending char and convert to float using list comprehension
    data = [float(x.rstrip()) for x in open(input_file)]

    # Create centroids
    centroids = dict(zip(range(k), data[0:k]))

    # Create clusters
    clusters = dict(zip(range(k), [[] for i in range(k)]))

    # Create point assignments
    point_assignments = []*k

    old_point_assignments = []*k
    point_assignments = assign_to_clusters(data, clusters, centroids, point_assignments)

    # Go through all of the point assignments and print them
    count = 0  # This count will increase as the number of iterations increases.
    while point_assignments != old_point_assignments:
        count += 1  # iterate count
        print "\n", "Iteration", count
        for a, b in clusters.items():
            print a, '', b
        new_centroids = update_centroids(clusters, centroids, k)
        old_point_assignments = list(point_assignments)
        # points = dict(old_point_assignments)
        clusters = dict(zip(range(k), [[] for i in range(k)]))
        point_assignments = assign_to_clusters(data, clusters, new_centroids, point_assignments)
    count += 1  # iterate count
    print "\n", "Iteration", count
    for a, b in clusters.items():
        print a, '', b

    # Print to output file
    output = open(output_file,'w')
    for x in range(len(point_assignments)):
        output.write('Point '+ repr(point_assignments[x][0])+ ' in cluster '+ repr(point_assignments[x][1])+ '\n')
    output.close()


if __name__ == "__main__":
    main()

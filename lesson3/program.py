import os
import random
import math

def lines_in_files(filename):
    x = 1
    try:
        if os.path.isfile(filename) == False:
            raise FileNotFoundError
    except FileNotFoundError:
        print("file not found!")
        return
    with open(filename,'r') as read_file, open("n_"+filename,'w') as write_file:
        for line_in_file in read_file:
            write_file.write(f"{x}. "+ line_in_file)
            x = x+1

def points(filename):
    points = {}
    try:
        if os.path.isfile(filename) == False:
            raise FileNotFoundError
    except FileNotFoundError:
        print("file not found!")
        return
    with open(filename,'r') as read_file:
        for line in read_file:
            a, *b = line.split()
            points[a] = b
    return points

def center(points):
    x = 0
    y = 0
    z = 0
    total = 0
    for point in points:
        x = x + float(point[1][0])
        y = y + float(point[1][1])
        z = z + float(point[1][2])
        total = total + 1
    result = [x/total, y/total, z/total]

    return result

def euclidean_distance(p, q):
    x = pow(float(p[0]) - float(q[0]), 2)
    y = pow(float(p[1]) - float(q[1]), 2)
    z = pow(float(p[2]) - float(q[2]), 2)
    d = math.sqrt(x+y+z)
    return d

def k_means(points,k):
    centroids = []
    test = []
    euclids = {}
    while len(centroids) < 4:
        for x in range(0,k):
            entry_list = list(points.items())
            for entry in entry_list:
                test.append([entry[0],entry[1]])
                new_point = random.choice(test)
            centroids.append(new_point)  
        #euclids erase
    while True:
        for x in range(0,k):
            euclids[centroids[x][0]] = []
        for point in points:
            distance = 999
            position = ''
            for centroid in centroids:
                temp = euclidean_distance(centroid[1],points[point])
                if distance > temp:
                    distance = temp
                    position = centroid[0]
            
            euclids[position].append([point,points[point]])
        g_cent = []
        for euclid in euclids:
            g_cent.append(center(euclids[euclid]))
        if g_cent[0] == centroids[0][1] and g_cent[1] == centroids[1][1] and g_cent[2] == centroids[2][1] and g_cent[3] == centroids[3][1]:
           final_list = []
           for euclid in euclids:
               print(f"Point {euclid}: ", end="")
               values = euclids[euclid]
               for value in values:
                   print(f"{value[0]} ",end="")
               print("")
           return
        else:
            centroids[0][1] = g_cent[0]
            centroids[1][1] = g_cent[1]
            centroids[2][1] = g_cent[2]
            centroids[3][1] = g_cent[3]
        

lines_in_files("text.txt")
points = points("features.txt")
k_means(points,4)

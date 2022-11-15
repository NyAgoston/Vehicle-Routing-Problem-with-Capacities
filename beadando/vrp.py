import random
def distance(c1, c2):
    return abs(c1[0] - c1[1]) + abs(c2[0] - c2[1])
def transform_vrp(cities):
    tsp_dict = {}
    for i in range(len(cities)):
        for j in range(len(cities)):
            tsp_dict[(i, j)] = distance(cities[i], cities[j])
    return tsp_dict


def min_dist(a,size,distances,used):
    min = 10000
    index = 0
    
    for i in range(size):
              
        if i not in used and min > distances[(a, i)]:  
            min = distances[(a, i)]
            index = i
    
    return index 
        

def vrp(cities,distances,vehicles):
    
    used = []
    used.append(0)
    
    for j in range(vehicles):
        order = []
        order.append(0)
        used.append(min_dist(0, len(cities),distances,used))   
        order.append(min_dist(0, len(cities),distances,used))        
        for i in range(vehicles - 1):
            used.append(min_dist(order[i], len(cities),distances,used))
            order.append(min_dist(order[i], len(cities),distances,used))
        order.append(0)
        print(order)
    
    
    return
        

def main():
    vehicles = 4
    
    cities = [(456, 320), # location 0 - the depot
    (228, 0), # location 1
    (912, 0), # location 2
    (0, 80), # location 3
    (114, 80), # location 4
    (570, 160), # location 5
    (798, 160), # location 6
    (342, 240), # location 7
    (684, 240), # location 8
    (570, 400), # location 9    
    (912, 400), # location 10
    (114, 480), # location 11
    (228, 480), # location 12
    (342, 560), # location 13
    (684, 560), # location 14
    (0, 640), # location 15
    (798, 640)] # location 16
    
    distances = transform_vrp(cities)
    
    print(distances)
    # print(distances[(0, 0)])
    # print(distances[(0, 1)])
    # print(distances[(0, 2)])
    # print(distances[(1, 0)])
    # print(distances[(1, 1)])
    # print(distances[(1, 2)])
    
    vrp(cities,distances,vehicles)
    
main()
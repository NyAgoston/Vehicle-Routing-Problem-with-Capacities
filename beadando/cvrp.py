import random
import matplotlib.pyplot as plt
import numpy as np
def distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
def transform_tsp(tsp):
    tsp_dict = {}
    for i in range(len(tsp)):
        for j in range(len(tsp)):
            tsp_dict[(i, j)] = distance(tsp[i], tsp[j])
    return tsp_dict
def makeArray(s,vehicles):
    rows, cols = (vehicles, ((len(s)) / vehicles) + 2)
    order = [[0 for i in range(int(cols))] for j in range(rows)]
    row = 0
    col = 0
    stop = len(s) / vehicles
    for i in s:
        order[row][col + 1] = i
        col += 1
        if col == int(stop):
            col = 0
            row += 1
    return order
def object_function(dict, s,vehicles):
    dist = 0
    cols = ((len(s)) / vehicles) + 2
    order = makeArray(s,vehicles)
    for j in range(vehicles):
        prev = order[j][0]
        for k in range(int(cols)):
            dist += dict[(prev, order[j][k])]
            prev = order[j][k]
    return dist
def calculateDemand(s,a,b,demands,capacities,vehicles):
    order = makeArray(s,vehicles)
    
    cols = ((len(s)) / vehicles) + 2
    for i in range(vehicles):
        if a in order[i] or b in order[i]:
            demand = 0
            for j in range(int(cols)):
                demand += demands[order[i][j]]
            if demand > capacities:
                return False

    return True
def neighborhood_search(s, object_f, iterations, neighbors,calculate_d):
    s_best = list(s)
    f_best = object_f(s)
    s_base = list(s_best)
    f_base = f_best
    for _ in range(iterations):
        s_best_neighbor = list(s_base)
        f_best_neighbor = f_base
        for i in range(neighbors):
            s_neighbor = list(s_base)
            a = random.randint(0, len(s) - 1)
            b = random.randint(0, len(s) - 1)
            s_neighbor[a], s_neighbor[b] = s_neighbor[b], s_neighbor[a]
            f_neighbor = object_f(s_neighbor)
            t = iterations / 1 + 0.8 * i
            diff = f_best_neighbor - f_neighbor
            Pt = (-diff / t)
            print(Pt)
            if calculate_d(s_neighbor,a,b) and f_neighbor < f_best_neighbor:
                f_best_neighbor = f_neighbor
                s_best_neighbor = s_neighbor
        s_base = s_best_neighbor
        f_base = f_best_neighbor
        if f_base < f_best:
            f_best = f_base
            s_best = s_base
    return s_best
def closest_Order(order,tsp_dict,vehicles):
    prev = 0
    isnull = 0
    stop = len(order) / vehicles
    for i in range(len(order)):
        min = 10000
        index = 0
        if isnull == int(stop):
            isnull = 0
            prev = 0
        for j in range(len(order)):
            if tsp_dict[(prev,j + 1)] < min and j + 1 not in order:
                min = tsp_dict[(prev,j + 1)]
                index = j + 1
        order[i] = index
        prev = index
        isnull += 1
    return order
def distancePerVehicle(s,dict):
    dist = 0
    prev = s[0]
    for i in s:
        dist += dict[(prev, i)]
        prev = i
    return dist
def printRoutes(s,vehicles,object_f,demands,dict,cities):
    order = makeArray(s,vehicles)
    cols = len(s) / vehicles + 2
    for i in range(vehicles):
        print("Route for vehicle ",i,":",sep='')
        demand = 0
        for j in range(int(cols)):
            print(order[i][j] ," ",end='')
            demand += demands[order[i][j]]
        print()
        print("Distance of route:",distancePerVehicle(order[i],dict))
        print("Load of the route:",demand)
        print()
    print()
    print("Total distance:",object_f(s))
    plt.plot(cities[0][0], cities[0][1],marker="o")
    plt.annotate(0, (cities[0][0], cities[0][1]))
    for i in s:
        plt.plot(cities[i][0], cities[i][1],marker="o")
        plt.annotate(i, (cities[i][0], cities[i][1]))
    colors = ["r","g","b","y","c","m","k","purple","pink","brown"]
    for j in range(vehicles):
        for k in range(int(cols) - 1):
            xpoints = (cities[order[j][k]][0],cities[order[j][k + 1]][0])
            ypoints = (cities[order[j][k]][1],cities[order[j][k + 1]][1])
            plt.plot(xpoints,ypoints,color=colors[j])

    plt.show()

def initData(vehicles,cities_num):
    cities = [()] * (cities_num + 1)

    demands = [0] * (cities_num + 1)
    done = True
    while(done):
        for i in range(cities_num):
            num = random.randint(1,9)
            demands[i + 1] = num
        if sum(demands) % vehicles == 0:
            done = False
    capaciti = sum(demands) / vehicles
    for i in range(cities_num + 1):
        x = random.randint(0,1000)
        y = random.randint(0,1000)
        cities[i] = (x,y)
    return cities,demands,capaciti,vehicles
def main():
    cities,demands,vehicle_capacities,vehicles = initData(4,16)
    
    vrp_dict = transform_tsp(cities)

    object_f = lambda sched: object_function(vrp_dict, sched,vehicles)

    calculate_d = lambda sched,a,b: calculateDemand(sched,b,a,demands,vehicle_capacities,vehicles)

    order = [0] * (len(cities) -1)

    i_order = closest_Order(order,vrp_dict,vehicles)
    
    # for i in range(16):
    #     i_order[i] = i + 1
    
    
    print(i_order)

    il_order = neighborhood_search(i_order,object_f,100,100,calculate_d)

    printRoutes(il_order,vehicles,object_f,demands,vrp_dict,cities)


main()
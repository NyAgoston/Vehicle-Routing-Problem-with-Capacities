import random
import math
import matplotlib.pyplot as plt

def distance(c1, c2): # Return distance between 2 cities
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
def transform_tsp(tsp): # Return an array that has every city conbination with distances
    tsp_dict = {}
    for i in range(len(tsp)):
        for j in range(len(tsp)):
            tsp_dict[(i, j)] = distance(tsp[i], tsp[j])
    return tsp_dict
def makeArray(s,vehicles): # Requires a 1d array and the num of vehicles
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
    return order # Return a n dimensonal array like: input->[1,2,3,4], vehicles = 2, return->[[1,2],[3,4]]
def object_function(dict, s,vehicles): #Requires the distances between cities, an order, num of vehicles
    dist = 0
    cols = ((len(s)) / vehicles) + 2
    order = makeArray(s,vehicles) # Generates a N dimensional array
    for j in range(vehicles):
        prev = order[j][0]
        for k in range(int(cols)):
            dist += dict[(prev, order[j][k])]
            prev = order[j][k]
    return dist # Returns the distance of given order
def calculateDemand(s,a,b,demands,capacities,vehicles):# Requires a order, two numbers, vehicle capacities, num of vehicles
    order = makeArray(s,vehicles) # Generates a N dimensional array
    
    cols = ((len(s)) / vehicles) + 2
    for i in range(vehicles): # If a or b is in sub array and the demand of sum array is greater than capaciti the return false
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
        for i in range(neighbors):# changing random indexes
            s_neighbor = list(s_base)
            a = random.randint(0, len(s) - 1)
            b = random.randint(0, len(s) - 1)
            s_neighbor[a], s_neighbor[b] = s_neighbor[b], s_neighbor[a]
            f_neighbor = object_f(s_neighbor)
            
            s_base = s_best_neighbor
            f_base = f_best_neighbor

            t = iterations / (1 + 0.8 * _) # simulated annelling

            #t = iterations / (1 + 0.8 * math.log(1) + _)
            plt.plot(t,_)                     
            if calculate_d(s_neighbor,s_neighbor[a],s_neighbor[b]) and f_neighbor < f_best_neighbor: # if changed order demand is true, and distance is less, switch the orders
                f_best_neighbor = f_neighbor
                s_best_neighbor = s_neighbor
            else:
                diff = f_best_neighbor - f_neighbor # simulated annelling
                Pt = (-diff / t) # simulated annelling
                if Pt > random.random(): # if true accept the worse solution
                    f_best_neighbor = f_neighbor
                    s_best_neighbor = s_neighbor    
        if f_base < f_best:
            f_best = f_base
            s_best = s_base   
    plt.show()
    return s_best
def closest_Order(order,tsp_dict,vehicles): # creates an order where every cities neighbour is the closest to itself
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

def initData(vehicles,cities_num): # Requires the num of vehicles, and the num of cities
    cities = [()] * (cities_num + 1)

    demands = [0] * (cities_num + 1)
    done = True
    while(done): # random demands for every city
        for i in range(cities_num):
            num = random.randint(1,9)
            demands[i + 1] = num
        if sum(demands) % vehicles == 0:
            done = False
    capaciti = sum(demands) / vehicles
    for i in range(cities_num + 1): # random coordinates for the every city
        x = random.randint(0,1000)
        y = random.randint(0,1000)
        cities[i] = (x,y)
    order = [0] * (len(cities) -1)
    #order = closest_Order(order,vrp_dict,vehicles)

    for i in range(len(cities) - 1): #generates a random order
        run = True
        while(run):
            num = random.randint(1,len(cities) - 1)
            if num not in order:
                run = False
        order[i] = num

    vrp_dict = transform_tsp(cities)

    object_f = lambda sched: object_function(vrp_dict, sched,vehicles)

    calculate_d = lambda sched,a,b: calculateDemand(sched,a,b,demands,capaciti,vehicles) 

    il_order = neighborhood_search(order,object_f,2000,100,calculate_d)

    return  il_order,vehicles,object_f,demands,vrp_dict,cities
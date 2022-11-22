import random

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
def calculateDemand(s,demands,capacities,vehicles):
    order = makeArray(s,vehicles)
    demand = 0
    cols = ((len(s)) / vehicles) + 2
    for i in range(vehicles):
        demand = 0
        for j in range(int(cols)):
            demand += demands[order[i][j]]
        if demand > capacities[0]:
            return False
    
    return True
def local_search(s, object_f, iterations,demands,capacities,vehicles):
    s_best = list(s)
    f_best = object_f(s)
    for _ in range(iterations):
        s_current = list(s_best)
        a = random.randint(0, len(s) - 1)
        b = random.randint(0, len(s) - 1)
        s_current[a], s_current[b] = s_current[b], s_current[a]
        f_current = object_f(s_current)
        t = iterations / 1 + 0.8 * _
        diff = f_best - f_current
        
        Pt = (-diff / t)    
        
        
        if calculateDemand(s_current,demands,capacities,vehicles) and f_current < f_best:
            f_best = f_current
            s_best = s_current
        # elif random.random() < Pt and calculateDemand(s_current,demands,capacities,vehicles):
        #     f_best = f_current
        #     s_best = s_current
    return s_best

def neighborhood_search(s, object_f, iterations, neighbors,demands,capacities,vehicles):
    s_best = list(s)
    f_best = object_f(s)
    s_base = list(s_best)
    f_base = f_best
    for _ in range(iterations):
        s_best_neighbor = list(s_base)
        f_best_neighbor = f_base
        for _ in range(neighbors):
            s_neighbor = list(s_base)
            a = random.randint(0, len(s) - 1)
            b = random.randint(0, len(s) - 1)
            s_neighbor[a], s_neighbor[b] = s_neighbor[b], s_neighbor[a]
            f_neighbor = object_f(s_neighbor)
            if f_neighbor < f_best_neighbor:
                f_best_neighbor = f_neighbor
                s_best_neighbor = s_neighbor
        s_base = s_best_neighbor
        f_base = f_best_neighbor
        
        if calculateDemand(s_base,demands,capacities,vehicles) and f_base < f_best:
            f_best = f_base
            s_best = s_base
    return s_best

def closest_Order(order,tsp_dict,vehicles):
    prev = 0
    isnull = 0
    stop = len(order) / vehicles + 2
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
def printRoutes(s,vehicles,object_f,demands,dict):
    order = makeArray(s,vehicles)
    for i in range(vehicles):
        print("Route for vehicle ",i,":",sep='')
        demand = 0
        for j in range(6):
            print(order[i][j] ," ",end='')
            demand += demands[order[i][j]]
        print()
        print("Distance of route:",distancePerVehicle(order[i],dict))
        print("Load of the route:",demand)
        print()
    print()
    print("Total distance:",object_f(s))
def main():
    demands = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    vehicle_capacities = [15, 15, 15, 15]
    vehicles = 4
    
    tsp = [(456, 320), # location 0 - the depot
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
            (0, 640),   # location 15
            (798, 640)] # location 16
    tsp_dict = transform_tsp(tsp)
    
    object_f = lambda sched: object_function(tsp_dict, sched,vehicles)
    
    
    order = [0] * (len(tsp) -1)
    
    
    i_order = closest_Order(order,tsp_dict,4)
    # print(i_order)
    # print(object_f(i_order))
    # print()
    
    ils_order = local_search(i_order,object_f,10000,demands,vehicle_capacities,vehicles)
    
    printRoutes(ils_order,4,object_f,demands,tsp_dict)
    #print(ils_order)
    # print(object_f(ils_order))
    # print()
    
    ins_order = neighborhood_search(i_order, object_f, 100, 100,demands,vehicle_capacities,vehicles)
    #printRoutes(ins_order,4,object_f,demands,tsp_dict)
    
    
    
    
main()

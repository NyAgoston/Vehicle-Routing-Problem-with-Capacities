def calculateDemand(s,demands,capacities,vehicles):
    order = makeArray(s,vehicles)
    demand = 0
    cols = ((len(s)) / vehicles) + 2
    for i in range(vehicles):
        demand = 0
        for j in range(int(cols)):
            demand += demands[order[i][j]]
        if demand > capacities:
            return False
    return True

demands = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    vehicle_capacities = 15
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
            (0, 640),   # location 15
            (798, 640)] # location 16
import random
def distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
def transform_tsp(tsp):
    tsp_dict = {}
    for i in range(len(tsp)):
        for j in range(len(tsp)):
            tsp_dict[(i, j)] = distance(tsp[i], tsp[j])
    return tsp_dict
def object_function(dict, s):
    dist = 0
    prev = s[0]
    for i in s:
        dist += dict[(prev, i)]
        prev = i
    dist += dict[(s[-1], s[0])]
    return dist
def local_search(s, object_f, iterations):
    s_best = list(s)
    f_best = object_f(s)
    for _ in range(iterations):
        s_current = list(s_best)
        a = random.randint(1, len(s) - 2)
        b = random.randint(1, len(s) - 2)
        s_current[a], s_current[b] = s_current[b], s_current[a]
        f_current = object_f(s_current)
        if f_current < f_best:
            f_best = f_current
            s_best = s_current
    return s_best
def main():
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
    s_bad = [0, 4, 2, 6, 5, 3, 7, 1]
    #print(tsp_dict)
    #print(object_function(tsp_dict, s_bad))
    s_opt = [0, 1, 2, 3, 4, 5, 6, 7]
    #print(object_function(tsp_dict, s_opt))
    object_f = lambda sched: object_function(tsp_dict, sched)
    
    tomb = [(0,1,2,0),(0,3,4,0),(0,5,6,0),(0,7,8,0)]
    
    rows, cols = (4, 6)
    order = [[0 for i in range(cols)] for j in range(rows)]
    
    print(order)
    
    num = 1
    for i in range(rows):
        for j in range(cols - 2):
            order[i][j + 1] = num
            num += 1  
    print(order)
    
    
    for i in range(rows):
        order[i] = local_search(order[i],object_f,10000)
    
    print(order)
            
main()
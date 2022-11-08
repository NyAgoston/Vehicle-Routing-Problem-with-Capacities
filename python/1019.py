import random
def distance(c1, c2):
    return ((c2[0] - c1[0])**2 + (c1[1] - c2[1])**2)**0.5
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
def neighborhood_search(s, object_f, iterations, neighbors):
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
        if f_base < f_best:
            f_best = f_base
            s_best = s_base
    return s_best
def main():
    tsp = ((1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3))
    tsp_dict = transform_tsp(tsp)
    s_bad = [0, 4, 2, 6, 5, 3, 7, 1]
    print(object_function(tsp_dict, s_bad))
    s_opt = [0, 1, 2, 3, 4, 5, 6, 7]
    print(object_function(tsp_dict, s_opt))
    object_f = lambda sched: object_function(tsp_dict, sched)
    s_improved = neighborhood_search(s_bad, object_f, 100, 100)
    print(object_function(tsp_dict, s_improved))
    print(s_bad, s_improved)
main()
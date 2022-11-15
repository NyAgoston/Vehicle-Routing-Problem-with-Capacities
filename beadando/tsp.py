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
def local_search(s, object_f, iterations):
    s_best = list(s)
    f_best = object_f(s)
    for _ in range(iterations):
        s_current = list(s_best)
        a = random.randint(0, len(s) - 1)
        b = random.randint(0, len(s) - 1)
        s_current[a], s_current[b] = s_current[b], s_current[a]
        f_current = object_f(s_current)
        if f_current < f_best:
            f_best = f_current
            s_best = s_current
    return s_best
def main():
    tsp = ((1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3))
    tsp_dict = transform_tsp(tsp)
    print(tsp_dict)
    s_bad = [0, 4, 2, 6, 5, 3, 7, 1]
    #print(object_function(tsp_dict, s_bad))
    s_opt = [0, 1, 2, 3, 4, 5, 6, 7]
    #print(object_function(tsp_dict, s_opt))
    object_f = lambda sched: object_function(tsp_dict, sched)
    s_improved = local_search(s_bad, object_f, 10000)
    print(s_improved)
    print(object_function(tsp_dict, s_improved))
    #print(s_bad, s_improved)
main()
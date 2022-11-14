import random

def manhattan(c1, c2):
    return ((c2[0] - c1[0])**2 + (c1[1] - c2[1])**2)**0.5

def transform_cities(cities):
    distances = {}
    for i in range(len(cities)):
        for j in range(len(cities)):
            distances[(i, j)] = manhattan(cities[i], cities[j])
    return distances

def object_function(distances, s):#gives back a distance
    dist = 0
    prev = s[0]
    for i in s:
        dist += distances[(prev, i)]
        prev = i
    dist += distances[(s[-1], s[0])]
    return dist

def local_search(s_bad, object_f, iterations):#gives back an order
    s_best = list(s_bad)
    f_best = object_f(s_bad)
    for _ in range(iterations):
        s_current = list(s_best)
        a = random.randint(0, len(s_bad) - 1)
        b = random.randint(0, len(s_bad) - 1)
        s_current[a], s_current[b] = s_current[b], s_current[a]
        f_current = object_f(s_current)
        if f_current < f_best:
            f_best = f_current
            s_best = s_current
    return s_best

def main():

    cities = ((1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3))

    distances = transform_cities(cities)

    s_bad = [0, 4, 2, 6, 5, 3, 7, 1]
    #print(object_function(distances, s_bad))

    s_opt = [0, 1, 2, 3, 4, 5, 6, 7]
    #print(object_function(distances, s_opt))
    
    object_f = lambda sched: object_function(distances, sched)#lambda distances

    s_improved = local_search(s_bad, object_f, 10000)#improved order

    print(object_function(distances, s_improved))#distances and best order    

main()
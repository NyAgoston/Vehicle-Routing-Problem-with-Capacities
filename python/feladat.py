from math import sqrt
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def solveVRP(cities,start,routes):    
    dist = 0
    if start == len(cities):
       return
    for i in range(int(routes)):
        print(start + i,"City:",cities[start + i])
        
        
    start += int(routes)
    solveVRP(cities,start,routes)
def main():
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
    
    start = 1
    routes = (len(cities) - 1) / 4
    
    solveVRP(cities,start,routes)  
main()
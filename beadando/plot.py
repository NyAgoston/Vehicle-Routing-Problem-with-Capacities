import matplotlib.pyplot as plt

def distancePerVehicle(s,dict):
    dist = 0
    prev = s[0]
    for i in s:
        dist += dict[(prev, i)]
        prev = i
    return dist

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
    
def printRoutes(s,vehicles,object_f,demands,dict,cities):
    order = makeArray(s,vehicles)
    cols = len(s) / vehicles + 2
    print("Demand per vehicle:",sum(demands)/vehicles)
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
    colors = ["r","g","b","y","c","m","k","purple","pink","brown","r","g","b","y","c","m","k","purple","pink","brown","r","g","b","y","c","m","k","purple","pink","brown"]
    for j in range(vehicles):
        for k in range(int(cols) - 1):
            xpoints = (cities[order[j][k]][0],cities[order[j][k + 1]][0])
            ypoints = (cities[order[j][k]][1],cities[order[j][k + 1]][1])
            plt.plot(xpoints,ypoints,color=colors[j])

    plt.show()
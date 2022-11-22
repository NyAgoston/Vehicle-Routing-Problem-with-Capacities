plt.plot(cities[0][0], cities[0][1],marker="o")
    plt.annotate(0, (cities[0][0], cities[0][1]))
    for i in s:
        plt.plot(cities[i][0], cities[i][1],marker="o")
        plt.annotate(i, (cities[i][0], cities[i][1]))
print()
    for i in range(rows):        
        for k in range(rows):
            order[i] = local_search(order[i][k],order[i][k],object_f,10000)
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res
    # raise NotImplementedError()

def jaccard_dist(x, y):
    bottom = 0
    top = 0
    for i in range(len(x)):
        if x[i]==y[i]:
            top+=1
        bottom +=1
    return 1-(abs(top) / abs(bottom))
    # raise NotImplementedError()

def cosine_sim(x, y):
    
    raise NotImplementedError()

# Feel free to add more

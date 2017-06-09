def extract_increasing_intervals(x):
    tmp = [[x[0]]]

    for i in range(1,len(x)):
        if x[i] >= x[i-1]:
            tmp[-1].append(x[i])
        else:
            tmp.append([x[i]])

    return tmp

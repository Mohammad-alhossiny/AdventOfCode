# by u/warbaque


from math import exp, log, ceil

def day_20(s):

    presents = int(s)

    def robins_inequality(n):
        return exp(0.57721566490153286060651209008240243104215933593992)*n*log(log(n))

    target = presents // 10

    lo = 5040
    hi = target
    while lo < hi:
        mid = (lo+hi)//2
        midval = robins_inequality(mid)
        if midval < target:
            lo = mid+1
        elif midval > target:
            hi = mid

    found = None
    while not found:

        lo = hi
        hi = int(lo*1.1)

        houses   = [i for i in range(lo, hi, 1)]
        n_houses = len(houses)
        visits   = [0]*n_houses

        end = n_houses
        for i in range(houses[-1], 1, -1):
            start = i*ceil(houses[0]/i)-houses[0]
            for j in range(start, end, i):
                visits[j] += i

        for i, s in enumerate(visits):
            if s > target:
                found = houses[0]+i
                break

    print(found)

day_20(34000000)
def fwht(a):
    h = 1
    while h < len(a):
        for i in range(0, len(a), h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j+h]
                a[j] = x + y
                a[j+h] = x - y
        h *= 2
    return a


def main():

    g1 = [0]
    g2 = [1,2,4,8]
    g3 = [3,9,12,6]
    g4 = [5,10]
    g5 = [7,11,13,14]
    g6 = [15]
    G = [g1,g2,g3,g4,g5,g6]
    print(G)

    for wt in range(14,16,2):

        for l in range(0,2**6):
            n = [int(i) for i in list(bin(l)[2:].zfill(6))]
            c = [x*y for x,y in zip(G,n)]
            d = sum([len(x) for x in c])
            if d == wt:
                e = [y for x in c for y in x]
                for m in range(0,2**6):
                    arr = [0]*16
                    for j in e:
                        arr[j] = 1
                    p = [int(i) for i in list(bin(m)[2:].zfill(6))]
                    for i in range(0,len(p)):
                        if p[i]:
                            for j in c[i]:
                                arr[j] = -1

                    arr = fwht(arr)
                    print(arr, sum(arr))
                    if sum(arr) == 4 or sum(arr) == -4:
                        print(n,c,e,arr)

if __name__ == "__main__":
    main()
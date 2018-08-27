n = 4

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
    g2 = [1,2,4,8,16,32]
    g3 = [3,6,12,24,48,33]
    g4 = [5,10,20,40,17,34]
    g5 = [7,14,28,56,49,35]
    g6 = [9,18,36]
    g7 = [11,22,44,25,50,37]
    g8 = [13,26,52,41,19,38]
    g9 = [15,30,60,57,49,39]
    g10 = [21,42]
    g11 = [23,46,29,58,53,43]
    g12 = [31,62,61,59,55,47]
    g13 = [45,27,54]
    g14 = [63]
    G = [g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14]

    for wt in range(0,256,2):
        print('weight : ', wt)

        for l in range(0,2**14):
            k = [int(i) for i in list(bin(l)[2:].zfill(14))]
            c = [x*y for x,y in zip(G,k)]
            d = sum([len(x) for x in c])
            if d == wt:
                e = [y for x in c for y in x]
                for m in range(0,2**14):
                    arr = [0]*64
                    for j in e:
                        arr[j] = 1
                    p = [int(i) for i in list(bin(m)[2:].zfill(14))]
                    for i in range(0,len(p)):
                        if p[i]:
                            for j in c[i]:
                                arr[j] = -1

                    arr = fwht(arr)
                    #print(arr, sum(arr))
                    if sum(arr) == 8 or sum(arr) == -8:
                        print(k,c,e,arr)

if __name__ == "__main__":
    main()

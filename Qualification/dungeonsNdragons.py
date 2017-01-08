# https://www.facebook.com/hackercup/problem/326053454264498/
__author__ = "Moonis Javed"
__email__ = "monis.javed@gmail.com"

from copy import copy

def findWays(m, n, x):
    table = [[0 for i in xrange(x+1)] for j in xrange(3)]
    j = 1
    while j <= m and j <= x:
        table[1][j] = 1
        j += 1
    for i in range(2,n+1):
        table[-1] = [0] * len(table[1])
        for j in range(1,x+1):
            k = 1
            while k <= m and k < j:
                table[-1][j] += table[1][j-k]
                k += 1
        table[1] = copy(table[-1])
    return table[-1]

if __name__ == "__main__":
    f = open("input1.txt").read().split("\n")
    writeF = open("output1.txt","w")
    n = int(f[0])
    del f[0]
    for i in range(1,n+1):
        h,s = [int(j) for j in f[0].split()]
        spells = f[1].split()
        del f[:2]
        probs = [0.000000 for num in xrange(s)]
        counter = 0
        for spell in spells:
            x = h
            n = int(spell.split("d")[0])
            m = int(spell.split("d")[1].split("+")[0].split("-")[0])
            if '+' in spell or '-' in spell:
                z = int(spell.split("+")[-1].split("-")[-1])
                if '+' in spell:
                    x -= z
                if '-' in spell:
                    x += z
            x = x - 1
            # print spell,h
            probs[counter] = (1 - (sum(findWays(m,n,x))/float(m**n)))
            counter += 1
        writeF.write("Case #%d: %.6f\n" % (i,max(probs)))
        print i
def mcnugg(n):
    for i in range (0, n//6+1):
        for j in range (0, n//9+1):
            for k in range (0, n//20+1):
                #print ("trying for %2d: %2d %2d %2d" % (n,i,j,k))
                if 6*i+9*j+20*k==n:
                    return (i,j,k)




print (mcnugg(80))

print (mcnugg(18))

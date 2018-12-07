class McNuggets:

    def __init__(self):
        pass

    @classmethod
    def calc(cls, n):
        
        print (cls)
        res="this is not mcnuggets number"
        for i in range (0, n//6+1):
            for j in range (0, n//9+1):
                for k in range (0, n//20+1):
                    #print ("trying for %2d: %2d %2d %2d" % (n,i,j,k))
                    if 6*i+9*j+20*k==n:
                        return (i, j, k)


        return res
mcn=McNuggets()
print(mcn)
print (McNuggets.calc(80))
print (McNuggets.calc(10))

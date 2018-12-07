class McNuggets:

    def __init__(self, n):
        self.n=n
        self.res= 'This is not a Mcnuggets number'


    def calc(self):

        for i in range (0, self.n//6+1):
            for j in range (0, self.n//9+1):
                for k in range (0, self.n//20+1):
                    #print ("trying for %2d: %2d %2d %2d" % (n,i,j,k))
                    if 6*i+9*j+20*k==self.n:
                        self.res= (i, j, k)
        # if self.res==():
        #     print( 'this is not a mcnuggets number')
        #

a=McNuggets(80)
b=McNuggets(18)
a.calc()
b.calc()
print (a.res)
print (b.res)

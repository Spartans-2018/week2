class McNuggets:
    def __init__(self, inlist):
        self.inlist = inlist

    def det_non_mcnuggets(self):
        reflist = [6,9,15,20,26,29,35]
        outlist = []
        ref_flag = 0
        for i in self.inlist:
            for ref in reflist:
                if i%ref ==0: ref_flag = 1
            if ref_flag == 0: outlist.append(i)
            ref_flag = 0

        return outlist

mcn = McNuggets([4,6,10,20,40, 35,26,45])
print(mcn.det_non_mcnuggets())





class CeaserDecoder:




    def coding(strin, key):
        cp=[]
        for i in strin:
            if i.isalpha()==True:
                ascii=ord(i)
                shift=ascii+key
                if shift in range (97, 123):
                    cp.append(chr(shift))
                elif shift>122:
                    cp.append(chr(shift-26))
                elif shift in range(65, 91):
                    cp.append(chr(shift))
                elif shift>90:
                    cp.append(chr(shift-26))
            else:
                cp.append(i)
        print (''.join(cp))



    def decoding (cstrin, key):
        cp=[]
        for i in cstrin:
            if i.isalpha()==True:
                ascii=ord(i)
                unshift=ascii-key
                if unshift in range (97, 123):
                    cp.append(chr(unshift))
                elif unshift in range(65, 91):
                    cp.append(chr(unshift))
                elif unshift<97:
                    cp.append(chr(unshift+26))

                elif shift<65:
                    cp.append(chr(unshift+26))
            else:
                cp.append(i)

        print (''.join(cp))
    # d=coding ('aB]Z',2)
    # print (d)

CeaserDecoder.coding ('zaAbc}Z.',2)
CeaserDecoder.decoding('bcCde}B', 2)

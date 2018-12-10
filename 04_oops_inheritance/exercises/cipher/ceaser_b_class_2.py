class CaeserDecoder:




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

# CaeserDecoder.coding ('zaAbc}Z.',2)
# CaeserDecoder.decoding('bcCde}B', 2)
# CaeserDecoder.decoding('cde', 2)

assert CaeserDecoder.decoding('cde', 2) == 'abc', 'cde - 2 should be abc'
assert CaeserDecoder.coding('abc', 2)=='cde'
assert CaeserDecoder.coding('!@#$%^&*()', 25)=='!@#$%^&*()'
assert CaeserDecoder.decoding('!@#$%^&*()', 25)=='!@#$%^&*()'
assert CaeserDecoder.decoding('CDE', 2) == 'ABC', 'CDE - 2 should be ABC'
assert CaeserDecoder.decoding('XYZ', 1) == 'WXY', 'XYZ - 1 should be WXY'
assert CaeserDecoder.coding('ABC', 1) == 'CDE', 'ABC +1  should be CDE'

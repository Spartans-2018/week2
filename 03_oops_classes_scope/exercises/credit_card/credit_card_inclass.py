class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = "a string"
        self.valid = 'a boolean'

# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        if len(self.card_number)<15 or len(self.card_number)>16:
            self.card_type='INVALID'
        elif int(self.card_number[0])==4:
            self.card_type = 'VISA'

        elif int (self.card_number[0:2])  in range(51,56):
            self.card_type= "MASTERCARD"
        elif int (self.card_number[0:2])== (34 or 37):
            self.card_type='AMEX'
        elif  int (self.card_number[0:4])==6001:
            self.card_type='DISCOVER'

        else:
            self.card_type='INVALID'

# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if len(self.card_number)==16:
            self.valid=True
        elif len(self.card_number)==15:
            self.valid=True
        else:
            self.valid=False

# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        ccl=list( int(i) for i in self.card_number )
        #print (ccl)

        for i in range (len(ccl)-2,-1, -2):
            if ccl[i]*2-10<0:
                ccl[i]= ccl[i]*2
            else:
                ccl[i]= 1+ccl[i]*2-10

        if sum(ccl)%10==0:
            self.valid = True
        else:
            self.valid = False





# ccb=CreditCard('4147202109113074')
# ccb=CreditCard('4147')
# ccb.validate ()
# ccb.check_length()
# ccb.determine_card_type()
# # print(cc.check_length())
# #print(cc.determine_card_type())
# print(ccb.valid)
# print(ccb.card_type)



# do not modify assert statements

cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

# cc = CreditCard('4440')
#
# assert cc.valid == False, "4440 is too short to be valid"
# assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')
# cc.validate ()
# cc.check_length()
# cc.determine_card_type()
assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

# cc = CreditCard('6011053711075799')

# assert cc.valid == True, "Discover Card is Valid"
# assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

# cc = CreditCard('379179199857686')

# assert cc.valid == True, "AMEX is Valid"
# assert cc.card_type == "AMEX", "card_type is AMEX"

# cc = CreditCard('4929896355493470')

# assert cc.valid == True, "Visa Card is Valid"
# assert cc.card_type == "VISA", "card_type is VISA"

# cc = CreditCard('4329876355493470')

# assert cc.valid == False, "This card does not meet mod10"
# assert cc.card_type == "INVALID", "card_type is INVALID"

# cc = CreditCard('339179199857685')

# assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
# assert cc.card_type == "INVALID", "card_type is INVALID"

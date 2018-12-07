class CreditCard:
    def __init__(self, ccnum):
        self.ccnum = ccnum

    def determine_card_type(self):
        if self.ccnum[0] == "4": return "Visa"
        elif self.ccnum[0:2] in ['51','52','53','54','55']: return "Mastercard"
        elif self.ccnum[0:2] in ['34','37']: return "AMEX"
        elif self.ccnum[0:4] in ['6011']: return "Discover"
        else: return "Unknown Type"

    def check_length(self):
        return(len(self.ccnum))

    def validate(self):
        a = self.ccnum[::-1]
        mynum = ""
        for i in range (len (a)):
            if i % 2 == 1: mynum += str (2 * int (a[i]))
            else: mynum += a[i]
        sumcc = sum (int(i) for i in list(mynum))
        if sumcc%10 !=0: return "Invalid Card Number"

        if self.determine_card_type() in ["Visa", "Mastercard", "Discover"] and self.check_length() !=16: return "Invalid Card Number"
        elif self.determine_card_type() in ["AMEX"] and self.check_length() !=15: return "Invalid Card Number"
        elif self.determine_card_type() not in ["Visa", "Mastercard", "AMEX", "Discover"]: return "Invalid Card Number"
        elif self.check_length() not in [15, 16]: return "Invalid Card Number"
        else: return "Valid Card Number"

cc = CreditCard("347650202246884")
print(cc.determine_card_type())
print(cc.check_length())
print(cc.validate())





# classes with different sort types 

class Bubble:
    
    def __init__(self):
        pass

    def sort(self, list):
        #""" sort list two-by-two until completely sorted """

        #sorting pair
        n=len(list)-1
        p=0
        r=0

        while n>0:
            for i in range(1, len(list)):
                if list[p]>list[i]:
                    list[p], list[i]= list[i], list[p]
                    p=p+1
                    n=n-1
                    r=r+1
                else:
                    p=p+1
                    n=n-1
        #repeating until no move made
        if r>0:
            self.sort(list)

        return list


class Merge:

    def __init__(self):
        pass

    def sort(self, list):
        # print('splitting', list)

        if len(list)>1:
            m=len(list)//2
            left_arr=list[:m]
            right_arr=list[m:]
            self.sort(left_arr)
            self.sort(right_arr)

            i=0
            j=0
            k=0

            #sorting
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    list[k]=left_arr[i]
                    i=i+1
                else:
                    list[k]=right_arr[j]
                    j=j+1
                k=k+1

            #merging
            while i < len(left_arr):
                list[k]=left_arr[i]
                i=i+1
                k=k+1

            while j < len(right_arr):
                list[k]=right_arr[j]
                j=j+1
                k=k+1
        
        return list


class Insertion:
    def __init__(self):
        pass

    def sort(self, list):
        """ sort list by comparing each value from left to right to the value of
         its left neighbor/s until a left value is less than the number. Swap indices
         for each comparison set in which left is greater than right. """

        for element in range(1, len(list)):
            j = element
            while j>0 and list[j-1]>list[j]:
                list[j-1], list[j]=list[j], list[j-1]
                j=j-1
                
        return list
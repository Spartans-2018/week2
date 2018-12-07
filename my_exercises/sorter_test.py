import sorter

# bubble_sort = sorter.Bubble()
# result1 = bubble_sort.sort([2, 3, 1, 9, 4])
# print("bubble sort: ")
# print (result1)

dictionary = {    
    'bubble': sorter.Bubble(),
    'merge': sorter.Merge(),
    'insertion': sorter.Insertion()
    }

def sort_by_algo(algo, list):
    
    result = dictionary[algo].sort(list)
    print(result)
    return result

list_to_sort =[678909876, 123456765432, 8765434567, 2345432, 123456765, -12345654, 0]

print("Bubble sort : *******************************")
sort_by_algo('bubble', list_to_sort)

print("Merge sort : *******************************")
sort_by_algo('merge', list_to_sort)

print("Insertion sort : *******************************")
sort_by_algo('insertion', list_to_sort)


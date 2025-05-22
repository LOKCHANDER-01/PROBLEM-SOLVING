#a=[1,2,[3,4,[5,6,[7,8,[9,10]]]]]
#Convert single list

a = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]

def numbers(b):
    for num in b:
        if isinstance(num, list):
            yield from numbers(num) 
        else:
            yield num
numbers_list = list(numbers(a))
print(numbers_list)